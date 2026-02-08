from sqlmodel import SQLModel, create_engine, Session
from typing import Generator
from contextlib import contextmanager
from src.config.settings import settings
import asyncio

# Import models to register them with SQLModel metadata
from src.models.task_model import Task
from src.models.user_model import User

# Create the database engine
engine = create_engine(settings.database_url, echo=True)

def create_db_and_tables_sync():
    """
    Create database tables if they don't exist.
    """
    SQLModel.metadata.create_all(engine)

async def create_db_and_tables():
    """
    Async version of create_db_and_tables for use with lifespan events.
    """
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    """
    Get a database session for use in endpoints.
    """
    with Session(engine) as session:
        yield session