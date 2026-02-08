import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))

from src.database.database import create_db_and_tables_sync
from src.models.user_model import User
from src.models.task_model import Task
from sqlmodel import select
from src.database import get_session

print("Testing database access...")

try:
    # Test creating tables
    create_db_and_tables_sync()
    print("[SUCCESS] Tables created/accessed successfully")

    # Test getting a session
    with get_session() as session:
        print("[SUCCESS] Database session acquired successfully")

        # Test querying users (might be empty)
        users = session.exec(select(User)).all()
        print(f"[SUCCESS] Successfully queried users, found {len(users)} users")

        # Test querying tasks (might be empty)
        tasks = session.exec(select(Task)).all()
        print(f"[SUCCESS] Successfully queried tasks, found {len(tasks)} tasks")

    print("[SUCCESS] All database tests passed!")

except Exception as e:
    print(f"[ERROR] Database test failed: {e}")
    import traceback
    traceback.print_exc()