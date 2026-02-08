# Quickstart Guide: Backend Core – Task Management API

## Setup Instructions

### 1. Prerequisites
- Python 3.13+
- Pip package manager
- Neon PostgreSQL account or local PostgreSQL installation

### 2. Environment Setup
1. Navigate to the backend directory
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Configuration
1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
2. Update the `.env` file with your database connection details:
   ```env
   DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/todo_db
   ```

### 4. Database Setup
1. Initialize the database:
   ```bash
   python -c "from src.database.database import create_db_and_tables; import asyncio; asyncio.run(create_db_and_tables())"
   ```
2. The database tables will be created automatically

### 5. Running the Application
Start the development server:
```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Usage Examples

### Create a Task
```bash
curl -X POST http://localhost:8000/api/user123/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, bread, eggs", "completed": false}'
```

### Get All Tasks for a User
```bash
curl http://localhost:8000/api/user123/tasks
```

### Get Tasks Filtered by Completion Status
```bash
curl "http://localhost:8000/api/user123/tasks?completed=true"
```

### Get a Specific Task
```bash
curl http://localhost:8000/api/user123/tasks/1
```

### Update a Task
```bash
curl -X PUT http://localhost:8000/api/user123/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries - urgent!", "completed": true}'
```

### Toggle Task Completion Status
```bash
curl -X PATCH http://localhost:8000/api/user123/tasks/1/complete
```

### Delete a Task
```bash
curl -X DELETE http://localhost:8000/api/user123/tasks/1
```

## Testing
Run the test suite:
```bash
python test_api.py
```

## Next Steps
- Implement JWT authentication in the next phase
- Add user management functionality
- Implement additional filtering and sorting options