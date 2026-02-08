# API Contracts: Backend Core – Task Management API

## Overview
REST API for task management with user scoping. All endpoints require user_id in the path for proper isolation between users.

## Base URL
`/api/{user_id}/tasks`

## Endpoints

### 1. Create Task
- **Method**: `POST`
- **Endpoint**: `/api/{user_id}/tasks`
- **Description**: Creates a new task for the specified user
- **Path Parameters**:
  - `user_id` (string): Unique identifier for the user
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
- **Description**: Retrieves all tasks for the specified user
- **Path Parameters**:
  - `user_id` (string): Unique identifier for the user
- **Query Parameters**:
  - `completed` (optional, boolean): Filter by completion status
- **Response Codes**:
  - `200 OK`: Successfully retrieved tasks
  - `404 Not Found`: User not found (if validation is implemented)
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
- **Description**: Retrieves a specific task by ID for the specified user
- **Path Parameters**:
  - `user_id` (string): Unique identifier for the user
  - `id` (integer): Task ID
- **Response Codes**:
  - `200 OK`: Task successfully retrieved
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
- **Description**: Updates a specific task by ID for the specified user
- **Path Parameters**:
  - `user_id` (string): Unique identifier for the user
  - `id` (integer): Task ID
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
- **Description**: Deletes a specific task by ID for the specified user
- **Path Parameters**:
  - `user_id` (string): Unique identifier for the user
  - `id` (integer): Task ID
- **Response Codes**:
  - `204 No Content`: Task successfully deleted
  - `404 Not Found`: Task not found or belongs to different user