# Data Model: Frontend Web Application – Task Management UI

## User Session Entity

### Fields
- **user_id**: String (Required) - Unique identifier for the authenticated user
- **token**: String (Required) - JWT token for API authentication
- **email**: String (Required) - User's email address
- **isLoggedIn**: Boolean (Required) - Authentication status
- **expiresAt**: Date (Required) - Token expiration timestamp

### State Transitions
- **Unauthenticated** → **Authenticating** → **Authenticated** → **Logging Out** → **Unauthenticated**
- **Token Refresh**: **Valid Token** → **Refreshing** → **New Token**

## Task Entity (Frontend Representation)

### Fields
- **id**: Number (Required) - Unique identifier for the task
- **user_id**: String (Required) - Link to the owning user
- **title**: String (Required, Max 200 chars) - Task title
- **description**: String (Optional) - Task description
- **completed**: Boolean (Required) - Completion status
- **created_at**: Date (Required) - Creation timestamp
- **updated_at**: Date (Required) - Last update timestamp

### State Transitions
- **New Task** → **Creating** → **Created** (completed=false)
- **Created** → **Updating** → **Updated** (title/description changes)
- **Created/Updated** → **Toggling** → **Updated** (completed status changes)
- **Created/Updated** → **Deleting** → **Deleted**

## API Client Entity

### Fields
- **baseUrl**: String (Required) - Base URL for API endpoints
- **headers**: Object (Required) - Default headers including authorization
- **timeout**: Number (Required) - Request timeout in milliseconds
- **retryAttempts**: Number (Required) - Number of retry attempts for failed requests

### Methods
- **get()**: Make GET request to API
- **post()**: Make POST request to API
- **put()**: Make PUT request to API
- **delete()**: Make DELETE request to API
- **patch()**: Make PATCH request to API

## UI State Entity

### Fields
- **isLoading**: Boolean (Required) - Loading state indicator
- **hasError**: Boolean (Required) - Error state indicator
- **errorMessage**: String (Optional) - Error message details
- **successMessage**: String (Optional) - Success message details
- **data**: Any (Optional) - Fetched data
- **lastUpdated**: Date (Optional) - Last data update timestamp

### State Transitions
- **Idle** → **Loading** → **Success/Data Received** / **Error**
- **Success** → **Reloading** → **Updated Data** / **Error**