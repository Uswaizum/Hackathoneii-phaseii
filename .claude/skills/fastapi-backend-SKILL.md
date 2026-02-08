name: backend-api
description: Generate FastAPI routes, handle HTTP requests and responses, and connect backend logic to the database using SQLModel. Use for implementing REST APIs.

---

# Backend API Implementation

## Instructions

1. **Route Generation**
   - Create RESTful routes under `/api/`
   - Follow HTTP method semantics (GET, POST, PUT, PATCH, DELETE)
   - Use path and query parameters correctly

2. **Request & Response Handling**
   - Validate requests using Pydantic models
   - Return structured JSON responses
   - Handle errors using `HTTPException`
   - Use appropriate status codes

3. **Database Connectivity**
   - Connect to Neon PostgreSQL via environment variable
   - Use SQLModel for all database operations
   - Perform CRUD operations safely
   - Ensure queries are scoped to authenticated users

4. **Authentication Awareness**
   - Expect authenticated user context from JWT middleware
   - Enforce user ownership on all operations
   - Reject unauthorized access

## Best Practices
- Keep route handlers small and focused
- Separate routing, models, and database logic
- Avoid raw SQL unless explicitly required
- Use dependency injection for DB sessions
- Follow specs under `/specs/api/` and `/specs/database/`

## Example Structure
```python
@router.post("/tasks")
def create_task(task: TaskCreate, user=Depends(get_current_user)):
    with Session(engine) as session:
        db_task = Task(user_id=user.id, **task.dict())
        session.add(db_task)
        session.commit()
        session.refresh(db_task)
        return db_task
