"""
Console Todo Application - Sorting Utilities

This module provides sorting functions for the todo application.
"""
from datetime import date
from typing import List, Callable
from ..models.task import Task, Priority


def sort_tasks_by_id(tasks: List[Task], ascending: bool = True) -> List[Task]:
    """
    Sort tasks by ID.

    Args:
        tasks: List of tasks to sort
        ascending: Sort order (True=ascending, False=descending)

    Returns:
        Sorted list of tasks
    """
    return sorted(tasks, key=lambda task: task.id, reverse=not ascending)


def sort_tasks_by_title(tasks: List[Task], ascending: bool = True) -> List[Task]:
    """
    Sort tasks by title.

    Args:
        tasks: List of tasks to sort
        ascending: Sort order (True=ascending, False=descending)

    Returns:
        Sorted list of tasks
    """
    return sorted(tasks, key=lambda task: task.title.lower(), reverse=not ascending)


def sort_tasks_by_due_date(tasks: List[Task], ascending: bool = True) -> List[Task]:
    """
    Sort tasks by due date.

    Args:
        tasks: List of tasks to sort
        ascending: Sort order (True=ascending, False=descending)

    Returns:
        Sorted list of tasks
    """
    def sort_key(task):
        # If due date is None, treat as the earliest possible date
        return task.due_date or date.min

    return sorted(tasks, key=sort_key, reverse=not ascending)


def sort_tasks_by_priority(tasks: List[Task], ascending: bool = True) -> List[Task]:
    """
    Sort tasks by priority.

    Args:
        tasks: List of tasks to sort
        ascending: Sort order (True=ascending, False=descending)

    Returns:
        Sorted list of tasks
    """
    # Define priority order: HIGH (0), MEDIUM (1), LOW (2)
    priority_order = {Priority.HIGH: 0, Priority.MEDIUM: 1, Priority.LOW: 2}

    def sort_key(task):
        return priority_order[task.priority]

    # For ascending, we want HIGH first, so we don't reverse the priority order
    # For descending, we want LOW first, so we reverse the priority order
    if ascending:
        return sorted(tasks, key=sort_key)
    else:
        return sorted(tasks, key=sort_key, reverse=True)


def sort_tasks_by_created_at(tasks: List[Task], ascending: bool = True) -> List[Task]:
    """
    Sort tasks by creation date.

    Args:
        tasks: List of tasks to sort
        ascending: Sort order (True=ascending, False=descending)

    Returns:
        Sorted list of tasks
    """
    def sort_key(task):
        return task.created_at or date.min

    return sorted(tasks, key=sort_key, reverse=not ascending)