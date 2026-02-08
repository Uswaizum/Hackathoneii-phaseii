from datetime import timedelta
from typing import Optional
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException, status, Depends
from jose import jwt


# Initialize HTTP Bearer scheme
security = HTTPBearer()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Get the current user from the JWT token in the Authorization header.
    """
    token = credentials.credentials
    try:
        from .jwt_handler import verify_access_token
        user_id = verify_access_token(token)
        return user_id
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


def validate_user_id_from_token(token_user_id: str, path_user_id: str):
    """
    Validate that the user_id from the token matches the user_id in the request path.
    This ensures users can only access their own data.
    """
    if token_user_id != path_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: You can only access your own resources",
        )


def decode_token_payload(token: str):
    """
    Decode the token payload without validation (for inspection purposes only).
    This should only be used for non-security critical operations.
    """
    try:
        payload = jwt.decode(token, options={"verify_signature": False})
        return payload
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not decode token payload",
            headers={"WWW-Authenticate": "Bearer"},
        )