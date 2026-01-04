# Data Model: Console Todo Application

## Overview
This document defines the data structures and relationships for the Console Todo Application, based on the functional requirements in the feature specification.

## Core Entities

### Task
**Definition**: A unit of work that users need to complete, containing all relevant information for task management.

**Attributes**:
- `id`: Unique identifier (integer, auto-generated, immutable)
- `title`: Task title (string, required, max 100 characters)
- `description`: Task description (string, optional, max 500 characters)
- `due_date`: Date when task is due (date object, optional)
- `priority`: Task priority level (enum: HIGH, MEDIUM, LOW, required)
- `tags`: List of tags associated with the task (list of strings, optional)
- `completed`: Completion status (boolean, default: False)
- `created_at`: Timestamp when task was created (datetime, auto-generated)
- `completed_at`: Timestamp when task was completed (datetime, optional)

**Validation Rules**:
- Title must be 1-100 characters (non-empty)
- Description, if provided, must be ≤ 500 characters
- Due date, if provided, must be in valid date format (YYYY-MM-DD)
- Priority must be one of: HIGH, MEDIUM, LOW
- Tags, if provided, must be valid strings (no empty tags)
- Each task must have a unique ID within the system

**State Transitions**:
- `pending` → `completed`: When user marks task as complete
- `completed` → `pending`: When user unmarks task as complete

### Priority (Enum)
**Definition**: Enumeration representing task priority levels.

**Values**:
- `HIGH`: Highest priority tasks
- `MEDIUM`: Medium priority tasks
- `LOW`: Lowest priority tasks

## Relationships

### Task to Tags
- One Task can have zero or more Tags
- Tags are stored as a list within each Task
- Tags are strings that help categorize tasks (e.g., "work", "personal", "urgent")

## Data Storage Structure

### In-Memory Storage Model
The application uses Python's built-in data structures for in-memory storage:

```python
# Internal representation
tasks: Dict[int, Task] = {}  # Dictionary mapping task IDs to Task objects
next_id: int = 1             # Counter for generating unique IDs
```

### Task Collection
- Tasks are stored in a dictionary with ID as key and Task object as value
- An ID counter ensures unique IDs are generated for new tasks
- No persistence - data exists only during runtime

## Business Rules

1. **Unique IDs**: Each task must have a unique ID that is auto-generated
2. **Required Fields**: Title is required for all tasks
3. **Validation**: All user inputs must be validated before creating/updating tasks
4. **Timestamps**: Creation timestamp is set automatically when task is created
5. **Completion Tracking**: Completion timestamp is set when task is marked complete
6. **Tag Management**: Duplicate tags on a single task are not allowed