"""
Console Todo Application - Formatting Utilities

This module provides formatting functions for displaying tasks in the todo application.
"""
from datetime import datetime
from typing import List
from ..models.task import Task, Priority


def format_task_list(tasks: List[Task]) -> str:
    """
    Format a list of tasks for display.

    Args:
        tasks: List of tasks to format

    Returns:
        Formatted string representation of the tasks
    """
    if not tasks:
        return "No tasks to display."

    # Calculate column widths
    max_id_width = max(2, len("ID"))  # At least 2 for "ID"
    max_title_width = max(10, len("Title"))  # At least 10 for "Title"
    max_status_width = max(8, len("Status"))  # At least 8 for "Status"
    max_priority_width = max(8, len("Priority"))  # At least 8 for "Priority"
    max_due_date_width = max(10, len("Due Date"))  # At least 10 for "Due Date"

    for task in tasks:
        max_id_width = max(max_id_width, len(str(task.id)))
        max_title_width = max(max_title_width, len(task.title))
        max_status_width = max(max_status_width, 3 if task.completed else 7)  # "Yes" or "Pending"
        max_priority_width = max(max_priority_width, len(task.priority.value))
        max_due_date_width = max(max_due_date_width, len(str(task.due_date) if task.due_date else "None"))

    # Create header
    header = (
        f"{'ID':<{max_id_width}} | "
        f"{'Title':<{max_title_width}} | "
        f"{'Status':<{max_status_width}} | "
        f"{'Priority':<{max_priority_width}} | "
        f"{'Due Date':<{max_due_date_width}} | Tags\n"
    )
    separator = (
        f"{'-' * max_id_width}-+-"
        f"{'-' * max_title_width}-+-"
        f"{'-' * max_status_width}-+-"
        f"{'-' * max_priority_width}-+-"
        f"{'-' * max_due_date_width}-+------\n"
    )

    result = header + separator

    # Add task rows
    for task in tasks:
        status = "Yes" if task.completed else "Pending"
        due_date_str = str(task.due_date) if task.due_date else "None"
        tags_str = ", ".join(task.tags) if task.tags else "None"

        result += (
            f"{task.id:<{max_id_width}} | "
            f"{task.title[:max_title_width]:<{max_title_width}} | "
            f"{status[:max_status_width]:<{max_status_width}} | "
            f"{task.priority.value[:max_priority_width]:<{max_priority_width}} | "
            f"{due_date_str[:max_due_date_width]:<{max_due_date_width}} | {tags_str}\n"
        )

    return result


def format_single_task(task: Task) -> str:
    """
    Format a single task for display.

    Args:
        task: Task to format

    Returns:
        Formatted string representation of the task
    """
    status = "Completed" if task.completed else "Pending"
    due_date_str = str(task.due_date) if task.due_date else "Not set"
    created_at_str = task.created_at.strftime("%Y-%m-%d %H:%M:%S") if task.created_at else "Unknown"
    completed_at_str = task.completed_at.strftime("%Y-%m-%d %H:%M:%S") if task.completed_at else "Not completed"

    tags_str = ", ".join(task.tags) if task.tags else "None"

    result = (
        f"ID: {task.id}\n"
        f"Title: {task.title}\n"
        f"Description: {task.description or 'None'}\n"
        f"Status: {status}\n"
        f"Priority: {task.priority.value}\n"
        f"Due Date: {due_date_str}\n"
        f"Created At: {created_at_str}\n"
        f"Completed At: {completed_at_str}\n"
        f"Tags: {tags_str}\n"
    )

    return result


def format_priority_indicator(priority: Priority) -> str:
    """
    Format a priority level with visual indicator.

    Args:
        priority: Priority level to format

    Returns:
        Formatted string with visual indicator
    """
    if priority == Priority.HIGH:
        return f"🔴 {priority.value}"
    elif priority == Priority.MEDIUM:
        return f"🟡 {priority.value}"
    else:  # LOW
        return f"🟢 {priority.value}"