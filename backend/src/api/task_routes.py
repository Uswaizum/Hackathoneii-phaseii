from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from sqlmodel import Session, select
from src.database import get_session
from src.models.task_model import Task, TaskCreate, TaskUpdate, TaskRead
from src.schemas.task_schemas import TaskCreateRequest, TaskUpdateRequest
from src.auth.auth_dependencies import require_same_user
from src.auth.security import get_current_user
import logging

# Configure logging
logger = logging.getLogger(__name__)

router = APIRouter()

def update_updated_at(task: Task):
    """Helper function to update the updated_at timestamp."""
    from datetime import datetime
    task.updated_at = datetime.utcnow()
    return task

@router.post("/tasks", response_model=TaskRead, status_code=201)
def create_task(
    task_data: TaskCreateRequest,
    user_id: str,
    current_user: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Create a new task for the specified user.
    Requires valid JWT authentication with matching user_id.
    """
    # Verify that the authenticated user matches the user_id in the path
    if current_user != user_id:
        raise HTTPException(
            status_code=403,
            detail="Access denied: You can only create tasks for yourself"
        )

    # Convert user_id from string (path param/JWT) to integer for database storage
    user_id_int = int(user_id)

    # Create task instance with user_id from path
    task = Task(
        user_id=user_id_int,
        title=task_data.title,
        description=task_data.description,
        completed=task_data.completed
    )

    session.add(task)
    session.commit()
    session.refresh(task)

    logging.info(f"Task created for user {user_id}: {task.title}")
    return task


@router.get("/tasks", response_model=List[TaskRead])
def read_tasks(
    user_id: str,
    completed: Optional[bool] = None,
    current_user: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Retrieve all tasks for the specified user.
    Requires valid JWT authentication with matching user_id.
    Optionally filter by completion status.
    """
    # Verify that the authenticated user matches the user_id in the path
    if current_user != user_id:
        raise HTTPException(
            status_code=403,
            detail="Access denied: You can only access your own tasks"
        )

    # Convert user_id from string (path param/JWT) to integer for database query
    user_id_int = int(user_id)

    # Build query filtering by user_id
    query = select(Task).where(Task.user_id == user_id_int)

    # Add completion filter if provided
    if completed is not None:
        query = query.where(Task.completed == completed)

    tasks = session.exec(query).all()

    logger.info(f"Retrieved {len(tasks)} tasks for user {user_id}")
    return tasks


@router.get("/tasks/{task_id}", response_model=TaskRead)
def read_task(
    user_id: str,
    task_id: int,
    current_user: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Retrieve a specific task by ID for the specified user.
    Requires valid JWT authentication with matching user_id.
    """
    # Verify that the authenticated user matches the user_id in the path
    if current_user != user_id:
        raise HTTPException(
            status_code=403,
            detail="Access denied: You can only access your own tasks"
        )

    # Convert user_id from string (path param/JWT) to integer for database query
    user_id_int = int(user_id)

    task = session.get(Task, task_id)

    # Check if task exists and belongs to the user
    if not task or task.user_id != user_id_int:
        logging.warning(f"User {user_id} tried to access task {task_id} which doesn't exist or belong to them")
        raise HTTPException(status_code=404, detail="Task not found or does not belong to user")

    logging.info(f"Task {task_id} accessed by user {user_id}")
    return task


@router.put("/tasks/{task_id}", response_model=TaskRead)
def update_task(
    user_id: str,
    task_id: int,
    task_data: TaskUpdateRequest,
    current_user: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Update a specific task by ID for the specified user.
    Requires valid JWT authentication with matching user_id.
    """
    # Verify that the authenticated user matches the user_id in the path
    if current_user != user_id:
        raise HTTPException(
            status_code=403,
            detail="Access denied: You can only update your own tasks"
        )

    # Convert user_id from string (path param/JWT) to integer for database query
    user_id_int = int(user_id)

    task = session.get(Task, task_id)

    # Check if task exists and belongs to the user
    if not task or task.user_id != user_id_int:
        logging.warning(f"User {user_id} tried to update task {task_id} which doesn't exist or belong to them")
        raise HTTPException(status_code=404, detail="Task not found or does not belong to user")

    # Update task fields if provided
    update_data = task_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        if value is not None:
            setattr(task, field, value)

    # Update the updated_at timestamp
    from datetime import datetime
    task.updated_at = datetime.utcnow()

    session.add(task)
    session.commit()
    session.refresh(task)

    logging.info(f"Task {task_id} updated by user {user_id}")
    return task


@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(
    user_id: str,
    task_id: int,
    current_user: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Delete a specific task by ID for the specified user.
    Requires valid JWT authentication with matching user_id.
    """
    # Verify that the authenticated user matches the user_id in the path
    if current_user != user_id:
        raise HTTPException(
            status_code=403,
            detail="Access denied: You can only delete your own tasks"
        )

    # Convert user_id from string (path param/JWT) to integer for database query
    user_id_int = int(user_id)

    task = session.get(Task, task_id)

    # Check if task exists and belongs to the user
    if not task or task.user_id != user_id_int:
        logging.warning(f"User {user_id} tried to delete task {task_id} which doesn't exist or belong to them")
        raise HTTPException(status_code=404, detail="Task not found or does not belong to user")

    session.delete(task)
    session.commit()

    logging.info(f"Task {task_id} deleted by user {user_id}")
    return


@router.patch("/tasks/{task_id}/complete", response_model=TaskRead)
def toggle_task_completion(
    user_id: str,
    task_id: int,
    current_user: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Toggle the completion status of a task.
    Requires valid JWT authentication with matching user_id.
    """
    # Verify that the authenticated user matches the user_id in the path
    if current_user != user_id:
        raise HTTPException(
            status_code=403,
            detail="Access denied: You can only update your own tasks"
        )

    # Convert user_id from string (path param/JWT) to integer for database query
    user_id_int = int(user_id)

    task = session.get(Task, task_id)

    # Check if task exists and belongs to the user
    if not task or task.user_id != user_id_int:
        logging.warning(f"User {user_id} tried to update task {task_id} which doesn't exist or belong to them")
        raise HTTPException(status_code=404, detail="Task not found or does not belong to user")

    # Toggle completion status
    task.completed = not task.completed

    # Update the updated_at timestamp
    from datetime import datetime
    task.updated_at = datetime.utcnow()

    session.add(task)
    session.commit()
    session.refresh(task)

    logging.info(f"Task {task_id} completion status toggled by user {user_id}")
    return task