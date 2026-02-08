# Todo Backend API

Backend API for the Todo application using FastAPI and SQLModel with Neon PostgreSQL.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy the environment file and update with your database connection and JWT configuration:
```bash
cp .env.example .env
# Edit .env to add your DATABASE_URL and JWT configuration
```

4. Start the development server:
```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Task Management

All endpoints follow the pattern `/api/{user_id}/tasks` for user isolation and require JWT authentication.

#### Create Task
- `POST /api/{user_id}/tasks`
- Creates a new task for the specified user
- Requires valid JWT with matching user_id in token

#### Get All Tasks
- `GET /api/{user_id}/tasks`
- Retrieves all tasks for the specified user
- Requires valid JWT with matching user_id in token
- Optional query parameter: `completed` (boolean) to filter by completion status

#### Get Task by ID
- `GET /api/{user_id}/tasks/{id}`
- Retrieves a specific task by ID for the specified user
- Requires valid JWT with matching user_id in token

#### Update Task
- `PUT /api/{user_id}/tasks/{id}`
- Updates a specific task by ID for the specified user
- Requires valid JWT with matching user_id in token

#### Delete Task
- `DELETE /api/{user_id}/tasks/{id}`
- Deletes a specific task by ID for the specified user
- Requires valid JWT with matching user_id in token

#### Toggle Task Completion
- `PATCH /api/{user_id}/tasks/{id}/complete`
- Toggles the completion status of a task
- Requires valid JWT with matching user_id in token

## Authentication

All API endpoints require JWT (JSON Web Token) authentication using the Bearer scheme.

### Making Authenticated Requests

Include the Authorization header in all requests:
```bash
curl -X GET http://localhost:8000/api/user123/tasks \
  -H "Authorization: Bearer YOUR_JWT_TOKEN_HERE"
```

### JWT Token Format

The JWT token must contain the following claims:
- `user_id`: The user identifier that must match the user_id in the URL
- `exp`: Expiration time of the token
- `sub`: Subject identifier (optional)

### Security Features

- Zero-trust authentication: Every request must be authenticated
- User isolation: Users can only access their own tasks
- Token validation: All tokens are cryptographically verified
- Expiration enforcement: Expired tokens are rejected

## Architecture

- **Framework**: FastAPI
- **ORM**: SQLModel
- **Database**: PostgreSQL (Neon)
- **API Design**: RESTful with proper HTTP status codes
- **Authentication**: JWT-based with stateless verification

## Features

- User isolation via user_id in all endpoints
- Automatic database table creation
- Input validation with Pydantic schemas
- Proper error handling with HTTP exceptions
- Timestamps for creation and updates
- CORS support for frontend communication
- JWT-based authentication and authorization
- Security headers for enhanced protection