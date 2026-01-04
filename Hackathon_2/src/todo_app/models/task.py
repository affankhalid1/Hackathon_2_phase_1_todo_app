"""
Console Todo Application - Task Model

This module defines the Task data model and related enums for the todo application.
"""
from dataclasses import dataclass
from datetime import datetime, date
from enum import Enum
from typing import List, Optional


class Priority(Enum):
    """Enumeration representing task priority levels."""
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


@dataclass
class Task:
    """A unit of work that users need to complete, containing all relevant information for task management."""

    id: int
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None
    priority: Priority = Priority.MEDIUM
    tags: List[str] = None
    completed: bool = False
    created_at: datetime = None
    completed_at: Optional[datetime] = None

    def __post_init__(self):
        """Initialize default values after object creation."""
        if self.tags is None:
            self.tags = []
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.completed and self.completed_at is None:
            self.completed_at = datetime.now()

        # Validate required fields
        self._validate_task()

    def _validate_task(self):
        """Validate task attributes."""
        if not self.title.strip():
            raise ValueError("Title must be non-empty")
        if len(self.title) > 100:
            raise ValueError("Title must be 100 characters or less")
        if self.description and len(self.description) > 500:
            raise ValueError("Description must be 500 characters or less")
        if self.priority not in [Priority.HIGH, Priority.MEDIUM, Priority.LOW]:
            raise ValueError("Priority must be one of HIGH, MEDIUM, or LOW")
        if self.tags and not all(isinstance(tag, str) and tag.strip() for tag in self.tags):
            raise ValueError("Tags must be non-empty strings")

    def update_title(self, title: str):
        """Update the task title after validation."""
        if not title.strip():
            raise ValueError("Title must be non-empty")
        if len(title) > 100:
            raise ValueError("Title must be 100 characters or less")
        self.title = title
        self._validate_task()

    def update_description(self, description: Optional[str]):
        """Update the task description after validation."""
        if description and len(description) > 500:
            raise ValueError("Description must be 500 characters or less")
        self.description = description
        self._validate_task()

    def update_priority(self, priority: Priority):
        """Update the task priority after validation."""
        if priority not in [Priority.HIGH, Priority.MEDIUM, Priority.LOW]:
            raise ValueError("Priority must be one of HIGH, MEDIUM, or LOW")
        self.priority = priority
        self._validate_task()

    def update_tags(self, tags: List[str]):
        """Update the task tags after validation."""
        if tags and not all(isinstance(tag, str) and tag.strip() for tag in tags):
            raise ValueError("Tags must be non-empty strings")
        self.tags = tags
        self._validate_task()

    def update_due_date(self, due_date: Optional[date]):
        """Update the task due date."""
        self.due_date = due_date
        self._validate_task()