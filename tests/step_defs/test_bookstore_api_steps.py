from pytest_bdd import scenarios, given, when, then, parsers
import requests
import pytest

# Scenarios
scenarios('../features/api/bookstore_api.feature')

# Fixtures
@pytest.fixture
def api_context():
    return {}

# Steps
@given('um usuário é criado com sucesso', target_fixture='user_context')
def create_user(config, api_context):
    base_url = config["base_url"].rstrip('/')
    user_payload = {
        "userName": "testuser_bdd",
        "password": "Password@123"
    }
    
    # Clean up before test: delete user if exists
    delete_response = requests.delete(f"{base_url}/Account/v1/UserByUserName/{user_payload['userName']}")
    
    response = requests.post(f"{base_url}/Account/v1/User", json=user_payload)
    assert response.status_code == 201, f"Failed to create user. Response: {response.text}"
    
    user = response.json()
    api_context['user'] = user
    api_context['user_payload'] = user_payload
    
    return api_context

@when('eu adiciono dois livros à sua coleção')
def add_books_to_collection(config, user_context):
    base_url = config["base_url"].rstrip('/')
    user_id = user_context['user']['userID']
    
    # Generate Token
    response = requests.post(f"{base_url}/Account/v1/GenerateToken", json=user_context['user_payload'])
    assert response.status_code == 200, f"Failed to generate token. Response: {response.text}"
    token = response.json()['token']
    auth_header = {'Authorization': f'Bearer {token}'}
    user_context['auth_header'] = auth_header

    # List Books
    response = requests.get(f"{base_url}/BookStore/v1/Books")
    assert response.status_code == 200, f"Failed to list books. Response: {response.text}"
    books = response.json()['books']
    assert len(books) > 1, "Not enough books available to perform the test."
    user_context['books_to_add'] = [books[0], books[1]]

    # Add two books
    books_to_add_payload = {
        "userId": user_id,
        "collectionOfIsbns": [
            {"isbn": books[0]['isbn']},
            {"isbn": books[1]['isbn']}
        ]
    }
    response = requests.post(f"{base_url}/BookStore/v1/Books", json=books_to_add_payload, headers=auth_header)
    assert response.status_code == 201, f"Failed to add books. Response: {response.text}"

@then('os livros devem ser listados nos detalhes do usuário')
def verify_books_in_user_details(config, user_context):
    base_url = config["base_url"].rstrip('/')
    user_id = user_context['user']['userID']
    auth_header = user_context['auth_header']

    response = requests.get(f"{base_url}/Account/v1/User/{user_id}", headers=auth_header)
    assert response.status_code == 200, f"Failed to get user details. Response: {response.text}"
    
    user_details = response.json()
    user_books_isbns = [book['isbn'] for book in user_details['books']]
    
    books_added = user_context['books_to_add']
    assert books_added[0]['isbn'] in user_books_isbns
    assert books_added[1]['isbn'] in user_books_isbns

    # Teardown
    requests.delete(f"{base_url}/Account/v1/User/{user_id}", headers=auth_header)