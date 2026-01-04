"""
Console Todo Application - Date Utilities

This module provides date-related utility functions for the todo application.
"""
from datetime import datetime, date
from typing import Optional


def parse_date(date_str: str) -> Optional[date]:
    """
    Parse a date string in YYYY-MM-DD format to a date object.

    Args:
        date_str: Date string in YYYY-MM-DD format

    Returns:
        Date object if valid, None otherwise
    """
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None


def format_date(date_obj: Optional[date]) -> str:
    """
    Format a date object to YYYY-MM-DD string.

    Args:
        date_obj: Date object to format

    Returns:
        Formatted date string or empty string if None
    """
    if date_obj is None:
        return ""
    return date_obj.strftime("%Y-%m-%d")


def is_date_overdue(due_date: Optional[date]) -> bool:
    """
    Check if a due date is in the past (overdue).

    Args:
        due_date: Due date to check

    Returns:
        True if overdue, False otherwise
    """
    if due_date is None:
        return False
    today = date.today()
    return due_date < today


def is_date_today(due_date: Optional[date]) -> bool:
    """
    Check if a due date is today.

    Args:
        due_date: Due date to check

    Returns:
        True if due date is today, False otherwise
    """
    if due_date is None:
        return False
    today = date.today()
    return due_date == today


def is_date_this_week(due_date: Optional[date]) -> bool:
    """
    Check if a due date is within the current week.

    Args:
        due_date: Due date to check

    Returns:
        True if due date is within the current week, False otherwise
    """
    if due_date is None:
        return False
    today = date.today()
    from datetime import timedelta
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)
    return week_start <= due_date <= week_end