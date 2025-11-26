import json
import pytest
from utils.webdriver_factory import WebDriverFactory
import requests

@pytest.fixture(scope="session")
def config():
    """
    Fixture to load the configuration file.
    """
    with open("config/config.json") as config_file:
        data = json.load(config_file)
    return data

@pytest.fixture(scope="session")
def driver(config):
    """
    Fixture to create and destroy the WebDriver instance.
    """
    browser = config["browser"]
    driver = WebDriverFactory.get_driver(browser)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def user_data(config):
    """Fixture to provide user data and clean up after tests."""
    base_url = config["base_url"].rstrip('/')
    user_payload = {
        "userName": "testuser_api",
        "password": "Password@123"
    }
    
    # Attempt to create a user
    response = requests.post(f"{base_url}/Account/v1/User", json=user_payload)
    
    # If user already exists, fail the test clearly.
    if response.status_code == 406 and "User exists" in response.text:
        pytest.fail("User 'testuser_api' already exists. Please clean up the test environment.")

    assert response.status_code == 201, f"Failed to create user. Response: {response.text}"
    user = response.json()
    yield user
    
    # Teardown: Delete the user
    token_response = requests.post(f"{base_url}/Account/v1/GenerateToken", json=user_payload)
    if token_response.status_code == 200:
        token = token_response.json()['token']
        auth_header = {'Authorization': f'Bearer {token}'}
        requests.delete(f"{base_url}/Account/v1/User/{user['userID']}", headers=auth_header)
