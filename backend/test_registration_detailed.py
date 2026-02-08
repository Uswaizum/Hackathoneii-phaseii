import requests
import traceback

def test_registration():
    try:
        print("Testing registration endpoint...")

        registration_data = {
            'email': 'testuser5@example.com',
            'name': 'Test User 5',
            'password': 'testpass123'
        }

        response = requests.post(
            'http://localhost:8000/api/v1/auth/register',
            json=registration_data,
            headers={
                'Content-Type': 'application/json'
            },
            timeout=10
        )

        print(f"Response Status: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        print(f"Response Text: {response.text}")

        if response.status_code == 201:
            print("[SUCCESS] Registration worked!")
            return True
        else:
            print(f"[ERROR] Registration failed with status {response.status_code}")
            return False

    except requests.exceptions.ConnectionError:
        print("[ERROR] Could not connect to server. Is it running on http://localhost:8000?")
        return False
    except Exception as e:
        print(f"[ERROR] Exception occurred: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_registration()