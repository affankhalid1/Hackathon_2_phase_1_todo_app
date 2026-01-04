# Internal API Contracts: Console Todo Application

## Overview
This document defines the internal interfaces and contracts for the Console Todo Application. Since this is a CLI application, these represent the internal service interfaces and data contracts.

## Task Model Interface

### Task Class Definition
```python
from dataclasses import dataclass
from datetime import datetime, date
from enum import Enum
from typing import List, Optional

class Priority(Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"

@dataclass
class Task:
    id: int
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None
    priority: Priority = Priority.MEDIUM
    tags: List[str] = None
    completed: bool = False
    created_at: datetime = None
    completed_at: Optional[datetime] = None
```

### Validation Rules
- `title` must be 1-100 characters (non-empty)
- `description` must be ≤ 500 characters if provided
- `due_date` must be in valid date format if provided
- `priority` must be one of Priority.HIGH, Priority.MEDIUM, Priority.LOW
- `tags` must not contain empty strings
- `id` must be unique within the system

## Task Service Interface

### TaskService Class
```python
from typing import List, Optional
from datetime import date

class TaskService:
    def __init__(self):
        pass

    def add_task(self, title: str, description: Optional[str] = None,
                 due_date: Optional[date] = None, priority: Priority = Priority.MEDIUM,
                 tags: Optional[List[str]] = None) -> Task:
        """Create a new task with the provided details."""
        # Returns the created Task with a unique ID and timestamps

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks in the system."""
        # Returns list of all tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Return a specific task by ID or None if not found."""
        # Returns Task or None

    def update_task(self, task_id: int, title: Optional[str] = None,
                    description: Optional[str] = None, due_date: Optional[date] = None,
                    priority: Optional[Priority] = None, tags: Optional[List[str]] = None) -> bool:
        """Update an existing task with provided fields."""
        # Returns True if successful, False if task not found

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID."""
        # Returns True if successful, False if task not found

    def mark_task_complete(self, task_id: int, completed: bool = True) -> bool:
        """Mark a task as complete or incomplete."""
        # Returns True if successful, False if task not found

    def search_tasks(self, keyword: str) -> List[Task]:
        """Search tasks by keyword in title or description."""
        # Returns list of matching tasks

    def filter_tasks(self, status: Optional[bool] = None,
                     priority: Optional[Priority] = None,
                     tags: Optional[List[str]] = None,
                     due_date_filter: Optional[str] = None) -> List[Task]:
        """Filter tasks based on provided criteria."""
        # Returns list of matching tasks

    def sort_tasks(self, sort_by: str, ascending: bool = True) -> List[Task]:
        """Sort tasks by specified field."""
        # Returns sorted list of tasks
```

## CLI Interface

### Menu Options Contract
The main menu provides the following numbered options:

1. `add_task` - Add a new task
2. `view_tasks` - View all tasks
3. `update_task` - Update an existing task
4. `delete_task` - Delete a task
5. `mark_complete` - Mark task as complete/incomplete
6. `search_tasks` - Search tasks by keyword
7. `filter_tasks` - Filter tasks by criteria
8. `sort_tasks` - Sort tasks by criteria
9. `exit` - Exit the application

### Input/Output Contract
- All user inputs are validated before processing
- Error messages are user-friendly and descriptive
- Task lists are displayed in a formatted, readable way
- Confirmation is required for destructive operations (delete)

## Error Handling Contract
- Invalid inputs result in appropriate error messages and re-prompting
- Attempting to access non-existent tasks results in appropriate feedback
- Date format errors result in clear guidance for correct format
- All errors are handled gracefully without application crashes