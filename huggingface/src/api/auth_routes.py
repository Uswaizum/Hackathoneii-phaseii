from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import Optional
from datetime import timedelta
from src.database import get_session
from src.models.user_model import User, UserCreate, UserLogin, Token, UserRead
from src.auth.jwt_handler import create_access_token, verify_password, hash_password
from src.auth.security import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
import logging

# Configure logging
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/register", response_model=Token, status_code=201)
def register_user(
    user_data: UserCreate,
    session: Session = Depends(get_session)
):
    """
    Register a new user.
    """
    # Check if user already exists
    existing_user = session.exec(
        select(User).where(User.email == user_data.email)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Hash the password
    hashed_password = hash_password(user_data.password)

    # Create new user
    user = User(
        email=user_data.email,
        name=user_data.name,
        hashed_password=hashed_password
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    logger.info(f"User registered: {user.email}")

    # Create access token
    access_token_expires = timedelta(minutes=86400)  # 24 hours
    access_token = create_access_token(
        data={"user_id": str(user.id)},  # Convert to string for consistency
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/login", response_model=Token)
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
):
    """
    Login user and return access token.
    """
    # Find user by email
    user = session.exec(
        select(User).where(User.email == form_data.username)
    ).first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    logger.info(f"User logged in: {user.email}")

    # Create access token
    access_token_expires = timedelta(minutes=86400)  # 24 hours
    access_token = create_access_token(
        data={"user_id": str(user.id)},  # Convert to string for consistency
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserRead)
def read_current_user(current_user: str = Depends(get_current_user), session: Session = Depends(get_session)):
    """
    Get current user information.
    """
    user_id = int(current_user)  # Convert back to int since it was stored as string in token

    user = session.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user