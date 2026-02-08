# API Contracts: Frontend Web Application – Task Management UI

## Overview
Frontend API contracts for interacting with the authenticated backend API. The frontend acts as a pure client of the backend API, following the API-driven UI principle.

## Authentication Endpoints
The frontend does not directly interact with authentication endpoints but relies on Better Auth for JWT token management.

## Task Management Endpoints

### 1. Create Task
- **Method**: `POST`
- **Endpoint**: `/api/{user_id}/tasks`
- **Authorization**: `Authorization: Bearer <jwt_token>`
- **Request Body**:
```json
{
  "title": "string (required, max 200 chars)",
  "description": "string (optional)",
  "completed": "boolean (optional, default false)"
}
```
- **Response Codes**:
  - `201 Created`: Task successfully created
  - `400 Bad Request`: Invalid input data
  - `401 Unauthorized`: Invalid or missing JWT token
  - `403 Forbidden`: User not authorized to access this resource
  - `404 Not Found`: User not found (if validation is implemented)
- **Success Response**:
```json
{
  "id": "integer",
  "user_id": "string",
  "title": "string",
  "description": "string or null",
  "completed": "boolean",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### 2. Get All Tasks
- **Method**: `GET`
- **Endpoint**: `/api/{user_id}/tasks`
- **Authorization**: `Authorization: Bearer <jwt_token>`
- **Query Parameters**:
  - `completed` (optional, boolean): Filter by completion status
- **Response Codes**:
  - `200 OK`: Successfully retrieved tasks
  - `401 Unauthorized`: Invalid or missing JWT token
  - `403 Forbidden`: User not authorized to access this resource
- **Success Response**:
```json
[
  {
    "id": "integer",
    "user_id": "string",
    "title": "string",
    "description": "string or null",
    "completed": "boolean",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
]
```

### 3. Get Task by ID
- **Method**: `GET`
- **Endpoint**: `/api/{user_id}/tasks/{id}`
- **Authorization**: `Authorization: Bearer <jwt_token>`
- **Response Codes**:
  - `200 OK`: Task successfully retrieved
  - `401 Unauthorized`: Invalid or missing JWT token
  - `403 Forbidden`: User not authorized to access this resource
  - `404 Not Found`: Task not found or belongs to different user
- **Success Response**:
```json
{
  "id": "integer",
  "user_id": "string",
  "title": "string",
  "description": "string or null",
  "completed": "boolean",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### 4. Update Task
- **Method**: `PUT`
- **Endpoint**: `/api/{user_id}/tasks/{id}`
- **Authorization**: `Authorization: Bearer <jwt_token>`
- **Request Body**:
```json
{
  "title": "string (optional, max 200 chars)",
  "description": "string (optional)",
  "completed": "boolean (optional)"
}
```
- **Response Codes**:
  - `200 OK`: Task successfully updated
  - `400 Bad Request`: Invalid input data
  - `401 Unauthorized`: Invalid or missing JWT token
  - `403 Forbidden`: User not authorized to access this resource
  - `404 Not Found`: Task not found or belongs to different user
- **Success Response**:
```json
{
  "id": "integer",
  "user_id": "string",
  "title": "string",
  "description": "string or null",
  "completed": "boolean",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### 5. Delete Task
- **Method**: `DELETE`
- **Endpoint**: `/api/{user_id}/tasks/{id}`
- **Authorization**: `Authorization: Bearer <jwt_token>`
- **Response Codes**:
  - `204 No Content`: Task successfully deleted
  - `401 Unauthorized`: Invalid or missing JWT token
  - `403 Forbidden`: User not authorized to access this resource
  - `404 Not Found`: Task not found or belongs to different user

### 6. Toggle Task Completion
- **Method**: `PATCH`
- **Endpoint**: `/api/{user_id}/tasks/{id}/complete`
- **Authorization**: `Authorization: Bearer <jwt_token>`
- **Response Codes**:
  - `200 OK`: Task completion status successfully toggled
  - `401 Unauthorized`: Invalid or missing JWT token
  - `403 Forbidden`: User not authorized to access this resource
  - `404 Not Found`: Task not found or belongs to different user
- **Success Response**:
```json
{
  "id": "integer",
  "user_id": "string",
  "title": "string",
  "description": "string or null",
  "completed": "boolean",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

## Frontend API Client Interface

### Expected Methods
The frontend API client should implement these methods:

- `createTask(userId: string, taskData: TaskCreateData)`: Promise<Task>
- `getTasks(userId: string, filters?: TaskFilters)`: Promise<Task[]>
- `getTask(userId: string, taskId: number)`: Promise<Task>
- `updateTask(userId: string, taskId: number, taskData: TaskUpdateData)`: Promise<Task>
- `deleteTask(userId: string, taskId: number)`: Promise<void>
- `toggleTaskCompletion(userId: string, taskId: number)`: Promise<Task>

### Error Handling Requirements
- Catch and handle 401 (Unauthorized) errors globally
- Catch and handle 403 (Forbidden) errors globally
- Display appropriate user feedback for different error types
- Implement retry logic for network-related errors
- Handle token expiration and trigger re-authentication flow

### Loading State Requirements
- Show loading indicators during API requests
- Disable user actions during in-flight requests
- Provide clear feedback when data is being fetched
- Handle optimistic updates where appropriate