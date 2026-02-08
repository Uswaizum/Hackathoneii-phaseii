import requests
import json

print("Final test of the Todo app functionality...")

# Test 1: Check basic server
try:
    response = requests.get("http://localhost:8000/")
    print(f"[SUCCESS] Basic server: {response.status_code} - {response.json()}")
except Exception as e:
    print(f"[ERROR] Basic server failed: {e}")

# Test 2: Check docs
try:
    response = requests.get("http://localhost:8000/docs")
    print(f"[SUCCESS] Docs endpoint: {response.status_code} (HTML response)")
except Exception as e:
    print(f"[ERROR] Docs endpoint failed: {e}")

# Test 3: Try registration with minimal data
try:
    registration_data = {
        "email": "finaltest@example.com",
        "name": "Final Test",
        "password": "test123"
    }

    response = requests.post(
        "http://localhost:8000/api/v1/auth/register",
        json=registration_data,
        headers={"Content-Type": "application/json"}
    )

    print(f"Registration attempt: Status {response.status_code}")
    if response.status_code == 201:
        token = response.json().get('access_token')
        print(f"[SUCCESS] Registration successful! Token: {token[:20]}...")
    else:
        print(f"[ERROR] Registration failed: {response.text}")

except Exception as e:
    print(f"[ERROR] Registration request failed: {e}")

print("\nTest completed!")