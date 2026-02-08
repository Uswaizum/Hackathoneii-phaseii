from src.models.user_model import User, UserCreate
from src.auth.jwt_handler import create_access_token, hash_password
from src.database import get_session
from sqlmodel import select

# Test creating a user manually to see if there are any issues
user_data = UserCreate(
    email="test@example.com",
    name="Test User",
    password="pass123"  # Very short password to avoid bcrypt 72-byte limit
)

print("Testing user creation...")

try:
    # Hash the password
    hashed_password = hash_password(user_data.password)
    print(f"[SUCCESS] Password hashed successfully: {hashed_password[:20]}...")

    # Create user object
    user = User(
        email=user_data.email,
        name=user_data.name,
        hashed_password=hashed_password
    )
    print(f"[SUCCESS] User object created: {user.email}, {user.name}")

    # Test saving to database
    with get_session() as session:
        print("[SUCCESS] Got database session")

        # Check if user already exists
        existing_user = session.exec(
            select(User).where(User.email == user_data.email)
        ).first()

        if existing_user:
            print(f"[INFO] User already exists: {existing_user.email}")
            session.delete(existing_user)
            session.commit()
            print("[INFO] Deleted existing user")

        # Add user to session
        session.add(user)
        session.commit()
        print(f"[SUCCESS] User saved to database with ID: {user.id}")

        # Refresh to get the ID
        session.refresh(user)
        print(f"[SUCCESS] User refreshed, ID: {user.id}")

        # Create access token
        access_token = create_access_token(
            data={"user_id": str(user.id)},
            expires_delta=None  # Use default
        )
        print(f"[SUCCESS] Access token created: {access_token[:20]}...")

    print("[SUCCESS] All auth tests passed!")

except Exception as e:
    print(f"[ERROR] Auth test failed: {e}")
    import traceback
    traceback.print_exc()