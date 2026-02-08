# Data Model: Backend Core – Task Management API

## Task Entity

### Fields
- **id**: Integer (Primary Key, Auto-generated)
- **user_id**: String (Indexed, Required) - Links task to specific user
- **title**: String (Required, Max 200 characters) - Task title
- **description**: Text (Optional) - Detailed task description
- **completed**: Boolean (Default: False) - Completion status
- **created_at**: DateTime (Auto-generated) - Timestamp of creation
- **updated_at**: DateTime (Auto-generated, Updates on change) - Timestamp of last update

### Relationships
- None (standalone entity with user_id for scoping)

### Validation Rules
- **title**: Required, maximum 200 characters
- **user_id**: Required, must be valid string identifier
- **completed**: Optional, defaults to False if not provided
- **description**: Optional, no length restriction

### State Transitions
- **Creation**: New task with completed=False, created_at and updated_at set to current time
- **Update**: Update task properties, updated_at set to current time
- **Completion**: Change completed from False to True
- **Reopening**: Change completed from True to False

## Indexes
- **user_id**: Index for efficient querying by user
- **(user_id, completed)**: Composite index for efficient filtering by user and completion status