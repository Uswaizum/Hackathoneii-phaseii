from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class User(SQLModel, table=True):
    """
    User model representing a registered user.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True, nullable=False)
    name: str = Field(max_length=100)
    hashed_password: str = Field(nullable=False)
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)



class UserCreate(SQLModel):
    """
    Model for creating new users.
    """
    email: str
    name: str
    password: str


class UserRegister(SQLModel):
    """
    Model for user registration.
    """
    email: str
    name: str
    password: str


class UserLogin(SQLModel):
    """
    Model for user login.
    """
    email: str
    password: str


class UserRead(SQLModel):
    """
    Model for returning user data without sensitive information.
    """
    id: int
    email: str
    name: str
    is_active: bool
    created_at: datetime
    updated_at: datetime


class Token(SQLModel):
    """
    Model for JWT token response.
    """
    access_token: str
    token_type: str = "bearer"


class TokenData(SQLModel):
    """
    Model for token data payload.
    """
    user_id: str