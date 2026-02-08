from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from fastapi import HTTPException, status
from ..config.settings import settings
import hashlib
import warnings


# Password hasher initialization (deferred until needed)
_pwd_context = None
_hash_method = None

def _get_password_hasher():
    global _pwd_context, _hash_method

    if _hash_method is None:  # Only initialize once
        try:
            from passlib.context import CryptContext
            pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
            # Test that it works
            pwd_context.hash("test")
            _pwd_context, _hash_method = pwd_context, "bcrypt"
        except Exception as e:
            warnings.warn(f"Bcrypt not available: {e}. Falling back to SHA-256 hashing for development.")
            _pwd_context, _hash_method = None, "sha256"

    return _pwd_context, _hash_method


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    Create an access token with the provided data and expiration time.
    """
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)

    to_encode.update({"exp": expire, "sub": str(to_encode.get("user_id", ""))})  # Add subject for compatibility
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


def verify_token(token: str):
    """
    Verify the JWT token and return the payload if valid.
    """
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        user_id: str = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return payload

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


def verify_access_token(token: str):
    """
    Verify the access token and return the user_id if valid.
    """
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        user_id: str = payload.get("user_id")

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return user_id

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


def hash_password(password: str):
    """
    Hash a password using bcrypt or SHA-256 as fallback.
    """
    pwd_context, hash_method = _get_password_hasher()

    if hash_method == "bcrypt":
        # Use bcrypt
        if pwd_context is None:
            raise RuntimeError("Password hashing is not available due to bcrypt initialization failure")

        # Truncate password to 72 bytes to comply with bcrypt limitation
        truncated_password = password[:72]
        try:
            return pwd_context.hash(truncated_password)
        except ValueError as e:
            if "password cannot be longer than 72 bytes" in str(e):
                # This shouldn't happen since we already truncate, but just in case
                return pwd_context.hash(password)
            else:
                raise
    elif hash_method == "sha256":
        # Use SHA-256 as fallback (NOT for production!)
        # This is only for development/testing when bcrypt fails
        salt = getattr(settings, 'secret_key', 'default_salt')[:10]  # Use first 10 chars of secret key as salt
        return hashlib.sha256((password + salt).encode()).hexdigest() + "_sha256"
    else:
        raise RuntimeError("No password hashing method available")


def verify_password(plain_password: str, hashed_password: str):
    """
    Verify a plain password against a hashed password.
    """
    pwd_context, hash_method = _get_password_hasher()

    if hash_method == "bcrypt":
        # Use bcrypt verification
        if pwd_context is None:
            raise RuntimeError("Password verification is not available due to bcrypt initialization failure")

        return pwd_context.verify(plain_password, hashed_password)
    elif hash_method == "sha256":
        # Verify using SHA-256 fallback (NOT for production!)
        # Check if the stored hash ends with our marker
        if hashed_password.endswith("_sha256"):
            expected_hash = hash_password(plain_password)
            return expected_hash == hashed_password
        else:
            # If the stored hash wasn't created with our fallback, it can't match
            return False
    else:
        raise RuntimeError("No password verification method available")