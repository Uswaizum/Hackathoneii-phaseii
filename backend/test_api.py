"""
Test script to verify the API endpoints work as expected.
This is a basic integration test to validate the functionality.
"""

import pytest
import asyncio
from fastapi.testclient import TestClient
from sqlmodel import Session, delete
from src.main import app
from src.database.database import engine, create_db_and_tables_sync
from src.models.task_model import Task

# Create test client
client = TestClient(app)

def setup_module():
    """Setup function to initialize the database."""
    create_db_and_tables_sync()

def teardown_module():
    """Teardown function to clean up the database."""
    with Session(engine) as session:
        statement = delete(Task)
        session.exec(statement)
        session.commit()

def test_create_task():
    """Test creating a new task."""
    response = client.post(
        "/api/user123/tasks",
        json={
            "title": "Test task",
            "description": "This is a test task",
            "completed": False
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test task"
    assert data["user_id"] == "user123"
    assert data["completed"] is False
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data

    # Store the created task ID for later tests
    global created_task_id
    created_task_id = data["id"]

def test_get_all_tasks():
    """Test getting all tasks for a user."""
    response = client.get("/api/user123/tasks")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    # Verify that we can find our created task
    task_titles = [task["title"] for task in data]
    assert "Test task" in task_titles

def test_get_specific_task():
    """Test getting a specific task."""
    response = client.get(f"/api/user123/tasks/{created_task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == created_task_id
    assert data["title"] == "Test task"
    assert data["user_id"] == "user123"

def test_update_task():
    """Test updating a task."""
    response = client.put(
        f"/api/user123/tasks/{created_task_id}",
        json={
            "title": "Updated task",
            "description": "This is an updated test task",
            "completed": True
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == created_task_id
    assert data["title"] == "Updated task"
    assert data["completed"] is True

def test_toggle_task_completion():
    """Test toggling task completion status."""
    response = client.patch(f"/api/user123/tasks/{created_task_id}/complete")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == created_task_id
    # Since we set it to True in the previous test, toggling should make it False
    assert data["completed"] is False

def test_delete_task():
    """Test deleting a task."""
    response = client.delete(f"/api/user123/tasks/{created_task_id}")
    assert response.status_code == 204  # No content on successful delete

    # Verify the task is gone
    response = client.get(f"/api/user123/tasks/{created_task_id}")
    assert response.status_code == 404

if __name__ == "__main__":
    # Run tests manually
    setup_module()

    try:
        test_create_task()
        print("✅ Create task test passed")

        test_get_all_tasks()
        print("✅ Get all tasks test passed")

        test_get_specific_task()
        print("✅ Get specific task test passed")

        test_update_task()
        print("✅ Update task test passed")

        test_toggle_task_completion()
        print("✅ Toggle task completion test passed")

        test_delete_task()
        print("✅ Delete task test passed")

        print("\n🎉 All API tests passed!")
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        raise
    finally:
        teardown_module()