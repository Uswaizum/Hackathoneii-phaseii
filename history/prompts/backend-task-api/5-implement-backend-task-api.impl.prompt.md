---
id: 5
title: Implement Backend Task API
stage: impl
date: 2026-01-16
surface: agent
model: Claude Sonnet 4.5
feature: backend-task-api
branch: 002-backend-task-api
user: s.c
command: /sp.implement
labels: [impl, backend, api, task-management]
links:
  spec: specs/backend-task-api/spec.md
  plan: specs/backend-task-api/plan.md
  tasks: specs/backend-task-api/tasks.md
  ticket: null
  adr: null
  pr: null
files:
 - backend/src/main.py
 - backend/src/config/settings.py
 - backend/src/database/database.py
 - backend/src/models/task_model.py
 - backend/src/schemas/task_schemas.py
 - backend/src/api/task_routes.py
 - backend/requirements.txt
 - backend/README.md
 - backend/CLAUDE.md
 - backend/.env.example
 - backend/.gitignore
 - backend/test_api.py
 - specs/backend-task-api/quickstart.md
tests:
 - backend/test_api.py
---

## Prompt

/sp.implement

Spec 1: Backend Core – Task Management API

Implementation Instructions:

Context:
You are implementing the backend foundation for Phase II of the Hackathon Todo App.
Follow Spec-Kit conventions and reference all relevant specs and CLAUDE.md files.

You MUST:
- Read @specs/overview.md
- Read @specs/features/task-crud.md
- Read @specs/api/rest-endpoints.md
- Read @specs/database/schema.md
- Follow @backend/CLAUDE.md guidelines

Implementation Steps:

1. Backend Project Setup
- Ensure /backend directory exists
- Create FastAPI app entry in main.py
- Enable CORS for frontend communication
- Load environment variables safely
- Expose app on port 8000

2. Database Layer
- Implement db.py using SQLModel
- Create engine using DATABASE_URL
- Implement get_session dependency
- Auto-create tables on startup

3. Data Models
- Implement Task SQLModel exactly as specified
- Include timestamps and defaults
- Ensure user_id is indexed
- Match schema spec strictly

4. API Schemas
- Create Pydantic models for:
  - TaskCreate
  - TaskUpdate
  - TaskRead
- Enforce validation rules (lengths, required fields)

5. Route Handlers
- Create routes under /api/{user_id}/tasks
- Implement all CRUD endpoints:
  - GET list
  - POST create
  - GET by id
  - PUT update
  - DELETE remove
  - PATCH toggle completion
- Filter all database queries by user_id
- Prevent cross-user access (return 404)

6. Error Handling
- Use HTTPException with proper status codes
- Return 422 for invalid input
- Return 404 for missing resources
- Ensure predictable JSON error responses

7. Readiness for Authentication
- Do NOT implement JWT validation yet
- Structure code so auth middleware can be added later
- Avoid hard-coding user identity logic

Verification Checklist:
- API starts without errors
- Tasks persist in database
- Multiple user_ids are isolated
- Endpoints behave exactly per spec

Output:
A production-ready FastAPI backend that fully satisfies Spec-1 and is ready for Spec-2 authentication integration.

## Response snapshot

Successfully implemented the complete Backend Core – Task Management API. Created all required components including FastAPI application, SQLModel database layer, Pydantic schemas, and complete CRUD endpoints with user isolation. The implementation follows all specified requirements with proper validation, error handling, and security measures. All 40 tasks from the task list were completed and marked as finished. Created comprehensive test file to validate functionality.

## Outcome

- ✅ Impact: Complete backend API implementation with all CRUD operations
- 🧪 Tests: Created test_api.py with comprehensive validation
- 📁 Files: All backend components created and integrated
- 🔁 Next prompts: Ready for authentication integration in next phase
- 🧠 Reflection: Implementation follows all spec requirements and best practices

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): standard implementation
- Next experiment (smallest change to try): add JWT authentication middleware