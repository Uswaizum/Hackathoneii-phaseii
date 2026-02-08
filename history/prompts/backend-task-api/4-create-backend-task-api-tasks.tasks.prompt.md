---
id: 4
title: Create Backend Task API Tasks
stage: tasks
date: 2026-01-16
surface: agent
model: Claude Sonnet 4.5
feature: backend-task-api
branch: 002-backend-task-api
user: s.c
command: /sp.tasks
labels: [tasks, backend, api, task-management]
links:
  spec: specs/backend-task-api/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/backend-task-api/tasks.md
tests:
 - none
---

## Prompt

/sp.tasks

Spec 1: Backend Core – Task Management API

Task Breakdown:

Task 1: Repository & Backend Skeleton
Owner: backend-architect

- Create /backend folder structure
- Initialize FastAPI app entry point (main.py)
- Add CLAUDE.md backend instructions
- Configure environment-based settings
- Verify app starts with uvicorn

Deliverable:
- Running FastAPI server with health check

---

Task 2: Database Configuration
Owner: database-engineer

- Configure DATABASE_URL from environment
- Initialize SQLModel engine and session
- Implement db.py connection layer
- Enable automatic table creation

Deliverable:
- Stable database connection to Neon PostgreSQL

---

Task 3: Data Models
Owner: database-engineer

- Define SQLModel Task table
- Add indexes on user_id and completed
- Add timestamps (created_at, updated_at)
- Ensure schema matches spec exactly

Deliverable:
- SQLModel Task model synced with database

---

Task 4: API Schemas
Owner: api-designer

- Create Pydantic request models
- Create Pydantic response models
- Enforce validation rules (lengths, required fields)
- Ensure models are JSON serializable

Deliverable:
- Validated request/response schemas

---

Task 5: CRUD Route Implementation
Owner: backend-developer

- Implement GET /api/{user_id}/tasks
- Implement POST /api/{user_id}/tasks
- Implement GET /api/{user_id}/tasks/{id}
- Implement PUT /api/{user_id}/tasks/{id}
- Implement DELETE /api/{user_id}/tasks/{id}
- Implement PATCH /api/{user_id}/tasks/{id}/complete
- Scope all queries by user_id
- Return correct HTTP status codes

Deliverable:
- Fully functional REST API endpoints

---

Task 6: Ownership Enforcement & Error Handling
Owner: backend-developer

- Prevent cross-user task access
- Return 404 for unauthorized task access
- Handle missing resources gracefully
- Validate invalid inputs (422)

Deliverable:
- Secure, predictable API behavior

---

Task 7: Verification & Readiness Check
Owner: qa-engineer

- Manually verify endpoints with multiple user_ids
- Confirm persistence across restarts
- Va

## Response snapshot

Generated complete task breakdown for the Backend Core – Task Management API at specs/backend-task-api/tasks.md. Organized tasks by user story priority (P1, P2, P3), included setup, foundational, and polish phases. Each task follows the required format with checkboxes, IDs, story labels, and specific file paths. Tasks are organized to enable parallel development and independent testing of each user story.

## Outcome

- ✅ Impact: Created complete task breakdown aligned with user stories and requirements
- 🧪 Tests: none
- 📁 Files: specs/backend-task-api/tasks.md created
- 🔁 Next prompts: Begin implementation of tasks
- 🧠 Reflection: Tasks organized for efficient parallel development

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): standard task creation
- Next experiment (smallest change to try): start implementing setup tasks