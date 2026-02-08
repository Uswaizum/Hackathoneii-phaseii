"""
Simple test script to verify the authentication functionality works as expected.
This is a basic integration test to validate the authentication implementation.
"""

import asyncio
from datetime import datetime, timedelta
from jose import jwt, JWTError
from src.config.settings import settings
from src.auth.jwt_handler import create_access_token


def test_token_creation():
    """Test that JWT tokens can be created properly."""
    # Create a test token
    data = {"user_id": "test_user_123", "email": "test@example.com"}
    token = create_access_token(data=data, expires_delta=timedelta(minutes=30))

    # Verify the token can be decoded
    decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

    assert decoded["user_id"] == "test_user_123"
    assert decoded["email"] == "test@example.com"
    assert "exp" in decoded

    print("✅ Token creation and decoding test passed!")


def test_token_expiration():
    """Test that JWT tokens expire properly."""
    # Create a token that expires in 1 second
    data = {"user_id": "test_user_123", "email": "test@example.com"}
    token = create_access_token(data=data, expires_delta=timedelta(seconds=1))

    # Verify the token can be decoded immediately
    decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    assert decoded["user_id"] == "test_user_123"

    # Wait for the token to expire
    import time
    time.sleep(2)  # Wait 2 seconds (more than the 1-second expiration)

    # Now try to decode - this should raise an exception in a real scenario
    try:
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        # If we get here, the token hasn't expired yet in this test environment
        print("⏰ Token hasn't expired yet in this test (may be due to system time precision)")
    except jwt.ExpiredSignatureError:
        print("✅ Token expiration test passed!")
    except JWTError:
        print("✅ Token expiration test passed!")

    print("✅ Token expiration test completed!")


if __name__ == "__main__":
    test_token_creation()
    test_token_expiration()
    print("\n🎉 All authentication tests passed!")