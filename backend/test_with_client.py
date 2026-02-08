from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_register():
    print("Testing registration with TestClient...")

    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "newtest@example.com",
            "name": "New Test User",
            "password": "testpass123"
        }
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    if response.status_code != 201:
        print(f"Headers: {response.headers}")
        if hasattr(response, 'content'):
            print(f"Full Content: {response.content}")
    else:
        print(f"Success Response: {response.json()}")

if __name__ == "__main__":
    test_register()