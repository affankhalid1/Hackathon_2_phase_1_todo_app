"""
Console Todo Application - Task Service

This module provides the business logic for task operations in the todo application.
"""
from datetime import date
from typing import List, Optional
from ..models.task import Task, Priority


class TaskService:
    """Service class for handling task business logic and operations."""

    def __init__(self):
        """Initialize the TaskService with in-memory storage."""
        self.tasks: dict[int, Task] = {}
        self.next_id: int = 1
        # Performance optimization: cache for search operations
        self._search_cache: dict[str, List[Task]] = {}

    def add_task(
        self,
        title: str,
        description: Optional[str] = None,
        due_date: Optional[date] = None,
        priority: Priority = Priority.MEDIUM,
        tags: Optional[List[str]] = None
    ) -> Task:
        """
        Create a new task with the provided details.

        Args:
            title: Task title
            description: Task description (optional)
            due_date: Task due date (optional)
            priority: Task priority (default: MEDIUM)
            tags: List of tags (optional)

        Returns:
            The created Task with a unique ID and timestamps

        Raises:
            ValueError: If task data is invalid
        """
        from datetime import datetime
        try:
            task = Task(
                id=self.next_id,
                title=title,
                description=description,
                due_date=due_date,
                priority=priority,
                tags=tags if tags is not None else [],
                created_at=datetime.now()
            )
            self.tasks[self.next_id] = task
            self.next_id += 1
            return task
        except ValueError as e:
            raise ValueError(f"Invalid task data: {str(e)}")

    def get_all_tasks(self) -> List[Task]:
        """
        Return all tasks in the system.

        Returns:
            List of all tasks
        """
        return list(self.tasks.values())

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Return a specific task by ID or None if not found.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            Task if found, None otherwise
        """
        return self.tasks.get(task_id)

    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        due_date: Optional[date] = None,
        priority: Optional[Priority] = None,
        tags: Optional[List[str]] = None
    ) -> bool:
        """
        Update an existing task with provided fields.

        Args:
            task_id: ID of the task to update
            title: New title (optional)
            description: New description (optional)
            due_date: New due date (optional)
            priority: New priority (optional)
            tags: New tags (optional)

        Returns:
            True if successful, False if task not found

        Raises:
            ValueError: If updated task data is invalid
        """
        if task_id not in self.tasks:
            return False

        try:
            task = self.tasks[task_id]
            if title is not None:
                task.update_title(title)
            if description is not None:
                task.update_description(description)
            if due_date is not None:
                task.update_due_date(due_date)
            if priority is not None:
                task.update_priority(priority)
            if tags is not None:
                task.update_tags(tags)

            return True
        except ValueError as e:
            raise ValueError(f"Invalid task data: {str(e)}")

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID.

        Args:
            task_id: ID of the task to delete

        Returns:
            True if successful, False if task not found
        """
        if task_id not in self.tasks:
            return False
        del self.tasks[task_id]
        return True

    def mark_task_complete(self, task_id: int, completed: bool = True) -> bool:
        """
        Mark a task as complete or incomplete.

        Args:
            task_id: ID of the task to update
            completed: Whether the task is completed (default: True)

        Returns:
            True if successful, False if task not found
        """
        if task_id not in self.tasks:
            return False

        task = self.tasks[task_id]
        task.completed = completed
        if completed:
            from datetime import datetime
            task.completed_at = datetime.now()
        else:
            task.completed_at = None

        return True

    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Search tasks by keyword in title or description.

        Args:
            keyword: The keyword to search for

        Returns:
            List of matching tasks
        """
        keyword = keyword.lower()
        matching_tasks = []
        for task in self.tasks.values():
            if keyword in task.title.lower() or (task.description and keyword in task.description.lower()):
                matching_tasks.append(task)
        return matching_tasks

    def filter_tasks(
        self,
        status: Optional[bool] = None,
        priority: Optional[Priority] = None,
        tags: Optional[List[str]] = None,
        due_date_filter: Optional[str] = None
    ) -> List[Task]:
        """
        Filter tasks based on provided criteria.

        Args:
            status: Filter by completion status (True=completed, False=pending, None=any)
            priority: Filter by priority level
            tags: Filter by tags (any of the tags)
            due_date_filter: Filter by date ('overdue', 'today', 'week', None)

        Returns:
            List of matching tasks
        """
        from ..utils.dates import is_date_overdue, is_date_today, is_date_this_week

        filtered_tasks = []
        for task in self.tasks.values():
            # Check status filter
            if status is not None and task.completed != status:
                continue

            # Check priority filter
            if priority is not None and task.priority != priority:
                continue

            # Check tags filter
            if tags:
                if not task.tags or not any(tag in task.tags for tag in tags):
                    continue

            # Check due date filter
            if due_date_filter == 'overdue' and not is_date_overdue(task.due_date):
                continue
            elif due_date_filter == 'today' and not is_date_today(task.due_date):
                continue
            elif due_date_filter == 'week' and not is_date_this_week(task.due_date):
                continue

            filtered_tasks.append(task)

        return filtered_tasks

    def sort_tasks(self, sort_by: str, ascending: bool = True) -> List[Task]:
        """
        Sort tasks by specified field.

        Args:
            sort_by: Field to sort by ('id', 'title', 'due_date', 'priority', 'created_at')
            ascending: Sort order (True=ascending, False=descending)

        Returns:
            Sorted list of tasks
        """
        def sort_key(task):
            if sort_by == 'id':
                return task.id
            elif sort_by == 'title':
                return task.title.lower()
            elif sort_by == 'due_date':
                return task.due_date or date.min
            elif sort_by == 'priority':
                # High priority should come first
                priority_order = {Priority.HIGH: 0, Priority.MEDIUM: 1, Priority.LOW: 2}
                return priority_order[task.priority]
            elif sort_by == 'created_at':
                return task.created_at
            else:
                return task.id  # Default to ID if unknown sort field

        return sorted(self.tasks.values(), key=sort_key, reverse=not ascending)