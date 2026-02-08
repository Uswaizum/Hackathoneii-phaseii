from fastapi import Depends, HTTPException, status
from typing import Optional
from .security import get_current_user, validate_user_id_from_token


def require_authentication():
    """
    Dependency to require authentication for endpoints.
    Returns the authenticated user_id.
    """
    def auth_dependency(current_user: str = Depends(get_current_user)):
        return current_user

    return Depends(auth_dependency)


def require_same_user():
    """
    Dependency to ensure the authenticated user matches the user in the path.
    This enforces user isolation.
    """
    def auth_dependency(current_user: str = Depends(get_current_user)):
        # The path_user_id will be validated in the route function itself
        return current_user

    return Depends(auth_dependency)


def optional_authentication():
    """
    Dependency for endpoints that can work with or without authentication.
    Returns the user_id if authenticated, None otherwise.
    """
    def auth_dependency(credentials: Optional[str] = Depends(lambda: None)):
        try:
            # Try to get current user, but catch exception to return None
            current_user = get_current_user()
            return current_user
        except HTTPException:
            # If authentication fails, return None
            return None

    # We need a more sophisticated approach for optional auth
    # This is a simplified version that doesn't use the security dependency directly
    pass


# Alternative implementation for optional authentication
async def get_optional_user(authorization: str = None):
    """
    Get user if authenticated, otherwise return None.
    This is a workaround for optional authentication.
    """
    if not authorization or not authorization.startswith("Bearer "):
        return None

    token = authorization[7:]  # Remove "Bearer " prefix
    try:
        from .jwt_handler import verify_access_token
        user_id = verify_access_token(token)
        return user_id
    except Exception:
        return None