import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.database.database import create_db_and_tables_sync
from src.config.settings import settings

print(f"Database URL: {settings.database_url}")
print("Attempting to create database tables...")

try:
    create_db_and_tables_sync()
    print("Database tables created successfully!")
except Exception as e:
    print(f"Error creating database tables: {e}")
    import traceback
    traceback.print_exc()