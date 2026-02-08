from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Task(SQLModel, table=True):
    """
    Task model representing a todo item with user association.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(index=True)  # Links task to specific user (now integer to match user ID)
    title: str = Field(min_length=1, max_length=200)  # Required, max 200 chars
    description: Optional[str] = Field(default=None)  # Optional description
    completed: bool = Field(default=False)  # Default to False
    created_at: datetime = Field(default_factory=datetime.utcnow)  # Auto-generated
    updated_at: datetime = Field(default_factory=datetime.utcnow)  # Auto-generated and updates on change


class TaskCreate(SQLModel):
    """
    Model for creating new tasks.
    """
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None)
    completed: Optional[bool] = Field(default=False)


class TaskUpdate(SQLModel):
    """
    Model for updating existing tasks.
    """
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None)
    completed: Optional[bool] = Field(default=None)


class TaskRead(SQLModel):
    """
    Model for returning task data with ID and timestamps.
    """
    id: int
    user_id: int
    title: str
    description: Optional[str] = None
    completed: bool
    created_at: datetime
    updated_at: datetime