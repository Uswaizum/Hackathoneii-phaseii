import requests
import json

# Define the base URL for the API
BASE_URL = "http://localhost:8000/api"

def test_registration():
    """Test user registration"""
    print("Testing user registration...")
    registration_data = {
        "email": "test@example.com",
        "name": "Test User",
        "password": "securepassword123"
    }

    response = requests.post(f"{BASE_URL}/v1/auth/register", json=registration_data)
    print(f"Registration response: {response.status_code}")
    print(f"Registration data: {response.json()}")

    if response.status_code == 201:
        token = response.json().get('access_token')
        print(f"Registration successful! Token: {token[:20]}..." if token else "No token received")
        return token
    else:
        print(f"Registration failed: {response.text}")
        return None

def test_login():
    """Test user login"""
    print("\nTesting user login...")
    login_data = {
        "username": "test@example.com",
        "password": "securepassword123"
    }

    response = requests.post(f"{BASE_URL}/v1/auth/login", data=login_data)
    print(f"Login response: {response.status_code}")
    print(f"Login data: {response.json()}")

    if response.status_code == 200:
        token = response.json().get('access_token')
        print(f"Login successful! Token: {token[:20]}..." if token else "No token received")
        return token
    else:
        print(f"Login failed: {response.text}")
        return None

def test_create_task(token):
    """Test creating a task"""
    print("\nTesting task creation...")
    headers = {"Authorization": f"Bearer {token}"}
    task_data = {
        "title": "Test Task",
        "description": "This is a test task",
        "completed": False
    }

    # We need to get the user ID first
    user_response = requests.get(f"{BASE_URL}/v1/auth/me", headers=headers)
    if user_response.status_code == 200:
        user_id = user_response.json().get('id')
        print(f"User ID: {user_id}")

        response = requests.post(f"{BASE_URL}/v1/{user_id}/tasks", json=task_data, headers=headers)
        print(f"Task creation response: {response.status_code}")
        print(f"Task creation data: {response.json()}")

        if response.status_code == 201:
            print("Task created successfully!")
            return response.json().get('id')
        else:
            print(f"Task creation failed: {response.text}")
            return None
    else:
        print(f"Failed to get user info: {user_response.text}")
        return None

def test_get_tasks(token):
    """Test getting tasks"""
    print("\nTesting getting tasks...")
    headers = {"Authorization": f"Bearer {token}"}

    # We need to get the user ID first
    user_response = requests.get(f"{BASE_URL}/v1/auth/me", headers=headers)
    if user_response.status_code == 200:
        user_id = user_response.json().get('id')
        print(f"User ID: {user_id}")

        response = requests.get(f"{BASE_URL}/v1/{user_id}/tasks", headers=headers)
        print(f"Get tasks response: {response.status_code}")
        print(f"Tasks data: {response.json()}")

        if response.status_code == 200:
            print("Tasks retrieved successfully!")
            return response.json()
        else:
            print(f"Get tasks failed: {response.text}")
            return None
    else:
        print(f"Failed to get user info: {user_response.text}")
        return None

if __name__ == "__main__":
    print("Testing API endpoints...\n")

    # Try to login first (in case user already exists)
    token = test_login()

    # If login fails, try to register
    if not token:
        token = test_registration()
        if token:
            # If registration was successful, try to login again
            token = test_login()

    if token:
        print(f"\nUsing token: {token[:20]}...")

        # Test creating a task
        task_id = test_create_task(token)

        # Test getting tasks
        tasks = test_get_tasks(token)
    else:
        print("Failed to authenticate, cannot test task operations")