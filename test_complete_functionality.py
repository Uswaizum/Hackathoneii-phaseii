import requests
import json
import time

# Define the base URL for the API
BASE_URL = "http://localhost:8000/api/v1"

def test_complete_flow():
    print("Testing complete end-to-end functionality...\n")

    # Step 1: Register a new user
    print("Step 1: Registering a new user...")
    registration_data = {
        "email": "testuser@example.com",
        "name": "Test User",
        "password": "securepassword123"
    }

    response = requests.post(f"{BASE_URL}/auth/register", json=registration_data)
    print(f"Registration response: {response.status_code}")

    if response.status_code == 201:
        token = response.json().get('access_token')
        print(f"[SUCCESS] Registration successful! Token received: {token[:20]}...")
    else:
        print(f"[ERROR] Registration failed: {response.text}")
        return False

    # Step 2: Login with the registered user
    print("\nStep 2: Logging in with registered user...")
    login_data = {
        "username": "testuser@example.com",
        "password": "securepassword123"
    }

    response = requests.post(f"{BASE_URL}/auth/login", data=login_data)
    print(f"Login response: {response.status_code}")

    if response.status_code == 200:
        token = response.json().get('access_token')
        print(f"[SUCCESS] Login successful! New token: {token[:20]}...")
    else:
        print(f"[ERROR] Login failed: {response.text}")
        return False

    # Step 3: Get user info
    print("\nStep 3: Getting user information...")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/auth/me", headers=headers)
    print(f"Get user response: {response.status_code}")

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get('id')
        print(f"[SUCCESS] User info retrieved! User ID: {user_id}")
    else:
        print(f"[ERROR] Failed to get user info: {response.text}")
        return False

    # Step 4: Create a task
    print("\nStep 4: Creating a new task...")
    task_data = {
        "title": "Complete end-to-end test",
        "description": "This is a test task to verify the complete functionality",
        "completed": False
    }

    response = requests.post(f"{BASE_URL}/{user_id}/tasks", json=task_data, headers=headers)
    print(f"Create task response: {response.status_code}")

    if response.status_code == 201:
        task = response.json()
        task_id = task.get('id')
        print(f"[SUCCESS] Task created successfully! Task ID: {task_id}")
    else:
        print(f"[ERROR] Failed to create task: {response.text}")
        return False

    # Step 5: Get all tasks
    print("\nStep 5: Getting all tasks...")
    response = requests.get(f"{BASE_URL}/{user_id}/tasks", headers=headers)
    print(f"Get tasks response: {response.status_code}")

    if response.status_code == 200:
        tasks = response.json()
        print(f"[SUCCESS] Retrieved {len(tasks)} task(s)")
        if len(tasks) > 0:
            print(f"  First task: '{tasks[0]['title']}' (ID: {tasks[0]['id']})")
    else:
        print(f"[ERROR] Failed to get tasks: {response.text}")
        return False

    # Step 6: Get specific task
    print(f"\nStep 6: Getting specific task (ID: {task_id})...")
    response = requests.get(f"{BASE_URL}/{user_id}/tasks/{task_id}", headers=headers)
    print(f"Get specific task response: {response.status_code}")

    if response.status_code == 200:
        task = response.json()
        print(f"[SUCCESS] Specific task retrieved! Title: '{task['title']}'")
    else:
        print(f"[ERROR] Failed to get specific task: {response.text}")
        return False

    # Step 7: Update the task
    print(f"\nStep 7: Updating task (ID: {task_id})...")
    update_data = {
        "title": "Updated task - Complete end-to-end test",
        "completed": True
    }

    response = requests.put(f"{BASE_URL}/{user_id}/tasks/{task_id}", json=update_data, headers=headers)
    print(f"Update task response: {response.status_code}")

    if response.status_code == 200:
        updated_task = response.json()
        print(f"[SUCCESS] Task updated successfully! New title: '{updated_task['title']}', Completed: {updated_task['completed']}")
    else:
        print(f"[ERROR] Failed to update task: {response.text}")
        return False

    # Step 8: Toggle task completion
    print(f"\nStep 8: Toggling task completion (ID: {task_id})...")
    response = requests.patch(f"{BASE_URL}/{user_id}/tasks/{task_id}/complete", headers=headers)
    print(f"Toggle completion response: {response.status_code}")

    if response.status_code == 200:
        toggled_task = response.json()
        print(f"[SUCCESS] Task completion toggled! Now completed: {toggled_task['completed']}")
    else:
        print(f"[ERROR] Failed to toggle task completion: {response.text}")
        return False

    # Step 9: Delete the task
    print(f"\nStep 9: Deleting task (ID: {task_id})...")
    response = requests.delete(f"{BASE_URL}/{user_id}/tasks/{task_id}", headers=headers)
    print(f"Delete task response: {response.status_code}")

    if response.status_code == 204:
        print(f"[SUCCESS] Task deleted successfully!")
    else:
        print(f"[ERROR] Failed to delete task: {response.text}")
        return False

    print("\n" + "="*50)
    print("[SUCCESS] All tests passed! Complete end-to-end functionality verified.")
    print("="*50)
    return True

if __name__ == "__main__":
    success = test_complete_flow()
    if success:
        print("\n[SUCCESS] Todo app is fully functional!")
    else:
        print("\n[ERROR] Some functionality is not working properly.")