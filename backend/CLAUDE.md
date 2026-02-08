# Backend Development Guidelines

## Tech Stack
- **Framework**: FastAPI (Python 3.13+)
- **ORM**: SQLModel for database operations
- **Database**: Neon PostgreSQL (serverless)
- **API Design**: RESTful endpoints following OpenAPI standards

## Project Structure
```
backend/
├── src/
│   ├── models/           # Data models using SQLModel
│   ├── schemas/          # Pydantic schemas for validation
│   ├── database/         # Database connection and session management
│   ├── api/              # API route handlers
│   ├── config/           # Configuration and settings
│   └── main.py           # Application entry point
├── tests/
│   ├── unit/
│   ├── integration/
│   └── contract/
├── requirements.txt
├── .env.example
└── README.md
```

## Key Principles
1. **Stateless Design**: No server-side session storage; all state in database or client
2. **Environment Configuration**: All secrets/config via environment variables
3. **User Isolation**: All queries filtered by user_id to prevent cross-user access
4. **JWT-Ready**: Code structure prepared for JWT authentication integration
5. **RESTful Design**: Follow REST conventions with proper HTTP status codes

## Development Standards
- Use type hints throughout
- Validate all inputs using Pydantic schemas
- Handle errors with proper HTTPException responses
- Log important operations for debugging
- Write tests for all functionality

## Security Considerations
- Never expose raw database errors to clients
- Validate user_id format and existence where appropriate
- Sanitize all user inputs
- Prepare for JWT authentication in future iteration

## API Endpoint Pattern
All endpoints follow: `/api/{user_id}/tasks/{id}` pattern for proper user isolation.