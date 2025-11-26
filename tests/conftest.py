import json
import pytest
from utils.webdriver_factory import WebDriverFactory

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
