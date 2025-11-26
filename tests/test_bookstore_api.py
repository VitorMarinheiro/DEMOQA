import requests

def test_bookstore_workflow(config, user_data):
    """
    Tests the full bookstore API workflow:
    1. Create a user (handled by fixture).
    2. Generate a token.
    3. Authorize the user.
    4. List available books.
    5. Add two books to the user's collection.
    6. Verify the books were added to the user's details.
    """
    base_url = config["base_url"].rstrip('/')
    user_id = user_data['userID']
    
    # 2. Generate Token
    login_payload = {
        "userName": "testuser_api",
        "password": "Password@123"
    }
    response = requests.post(f"{base_url}/Account/v1/GenerateToken", json=login_payload)
    assert response.status_code == 200, f"Failed to generate token. Response: {response.text}"
    token = response.json()['token']
    auth_header = {'Authorization': f'Bearer {token}'}

    # 3. Confirm Authorization
    response = requests.post(f"{base_url}/Account/v1/Authorized", json=login_payload)
    assert response.status_code == 200, f"User is not authorized. Response: {response.text}"
    assert response.text == "true", "Authorization check failed."

    # 4. List Books
    response = requests.get(f"{base_url}/BookStore/v1/Books")
    assert response.status_code == 200, f"Failed to list books. Response: {response.text}"
    books = response.json()['books']
    assert len(books) > 1, "Not enough books available to perform the test."
    
    # 5. Add two books
    books_to_add = [
        {"isbn": books[0]['isbn']},
        {"isbn": books[1]['isbn']}
    ]
    add_books_payload = {
        "userId": user_id,
        "collectionOfIsbns": books_to_add
    }
    response = requests.post(f"{base_url}/BookStore/v1/Books", json=add_books_payload, headers=auth_header)
    assert response.status_code == 201, f"Failed to add books. Response: {response.text}"

    # 6. List user details and verify books
    response = requests.get(f"{base_url}/Account/v1/User/{user_id}", headers=auth_header)
    assert response.status_code == 200, f"Failed to get user details. Response: {response.text}"
    user_details = response.json()
    
    user_books_isbns = [book['isbn'] for book in user_details['books']]
    assert books[0]['isbn'] in user_books_isbns
    assert books[1]['isbn'] in user_books_isbns