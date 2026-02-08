name: database
description: Design database schema, create tables, and manage migrations using SQLModel with Neon Serverless PostgreSQL.

---

# Database Schema & Migrations

## Instructions

1. **Schema Design**
   - Define tables, columns, and relationships
   - Use appropriate data types and constraints
   - Enforce user ownership via foreign keys
   - Add indexes for frequently queried fields

2. **Table Creation**
   - Create tables using SQLModel models
   - Ensure schema matches specs exactly
   - Support multi-user data isolation

3. **Migrations**
   - Generate migrations for schema changes
   - Apply migrations safely without data loss
   - Keep database structure aligned with specs

4. **Neon PostgreSQL Integration**
   - Use serverless-compatible connection patterns
   - Read database URL from environment variables
   - Ensure reliable connection handling

## Best Practices
- Follow `/specs/database/schema.md` strictly
- Avoid raw SQL unless required by spec
- Keep schemas normalized and minimal
- Design for future schema evolution
- Maintain consistency between ORM and database

## Example Structure
```python
class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(index=True, foreign_key="users.id")
    title: str
    completed: bool = Field(default=False)

