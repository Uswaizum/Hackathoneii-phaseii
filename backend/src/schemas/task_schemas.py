from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskCreateRequest(BaseModel):
    """
    Schema for creating new tasks.
    """
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = False


class TaskUpdateRequest(BaseModel):
    """
    Schema for updating existing tasks.
    """
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None