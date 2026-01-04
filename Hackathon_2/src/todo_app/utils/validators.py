"""
Console Todo Application - Validation Utilities

This module provides validation functions for the todo application.
"""
from datetime import datetime
from typing import List, Optional
from ..models.task import Priority


def validate_title(title: str) -> bool:
    """
    Validate task title.

    Args:
        title: The title to validate

    Returns:
        True if valid, False otherwise
    """
    if not title or not title.strip():
        return False
    if len(title.strip()) > 100:
        return False
    return True


def validate_description(description: Optional[str]) -> bool:
    """
    Validate task description.

    Args:
        description: The description to validate (can be None)

    Returns:
        True if valid or None, False otherwise
    """
    if description is None:
        return True
    if len(description) > 500:
        return False
    return True


def validate_date(date_str: str) -> bool:
    """
    Validate date string in YYYY-MM-DD format.

    Args:
        date_str: The date string to validate

    Returns:
        True if valid, False otherwise
    """
    if not date_str:
        return False
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_priority(priority: str) -> bool:
    """
    Validate priority string.

    Args:
        priority: The priority string to validate

    Returns:
        True if valid, False otherwise
    """
    try:
        Priority[priority.upper()]
        return True
    except KeyError:
        return False


def validate_tags(tags: List[str]) -> bool:
    """
    Validate list of tags.

    Args:
        tags: The list of tags to validate

    Returns:
        True if valid, False otherwise
    """
    if not isinstance(tags, list):
        return False
    for tag in tags:
        if not isinstance(tag, str) or not tag.strip():
            return False
        if len(tag.strip()) == 0:
            return False
    return True


def validate_task_data(
    title: str,
    description: Optional[str] = None,
    due_date: Optional[str] = None,
    priority: Optional[str] = None,
    tags: Optional[List[str]] = None
) -> tuple[bool, List[str]]:
    """
    Validate all task data and return validation result and errors.

    Args:
        title: Task title
        description: Task description (optional)
        due_date: Task due date in YYYY-MM-DD format (optional)
        priority: Task priority (optional)
        tags: List of tags (optional)

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []

    if not validate_title(title):
        errors.append("Title must be 1-100 characters and not empty")

    if not validate_description(description):
        errors.append("Description must be 500 characters or less")

    if due_date and due_date.strip() and not validate_date(due_date):
        errors.append("Due date must be in YYYY-MM-DD format")

    if priority and priority.strip() and not validate_priority(priority):
        errors.append("Priority must be HIGH, MEDIUM, or LOW")

    if tags and not validate_tags(tags):
        errors.append("Tags must be a list of non-empty strings")

    return len(errors) == 0, errors