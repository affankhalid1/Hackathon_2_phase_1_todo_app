"""
Unit tests for the Task model in the Console Todo Application.
"""
import pytest
from datetime import datetime, date
from src.todo_app.models.task import Task, Priority


def test_task_creation():
    """Test creating a basic task."""
    task = Task(id=1, title="Test task")
    assert task.id == 1
    assert task.title == "Test task"
    assert task.completed is False
    assert task.priority == Priority.MEDIUM


def test_task_creation_with_all_fields():
    """Test creating a task with all fields."""
    test_date = date.today()
    task = Task(
        id=1,
        title="Test task",
        description="Test description",
        due_date=test_date,
        priority=Priority.HIGH,
        tags=["work", "urgent"]
    )
    assert task.id == 1
    assert task.title == "Test task"
    assert task.description == "Test description"
    assert task.due_date == test_date
    assert task.priority == Priority.HIGH
    assert "work" in task.tags
    assert "urgent" in task.tags


def test_task_validation_title_required():
    """Test that task title is required."""
    with pytest.raises(ValueError, match="Title must be non-empty"):
        Task(id=1, title="")


def test_task_validation_title_length():
    """Test that task title length is limited."""
    long_title = "x" * 101  # 101 characters, exceeding limit
    with pytest.raises(ValueError, match="Title must be 100 characters or less"):
        Task(id=1, title=long_title)


def test_task_validation_description_length():
    """Test that task description length is limited."""
    long_description = "x" * 501  # 501 characters, exceeding limit
    with pytest.raises(ValueError, match="Description must be 500 characters or less"):
        Task(id=1, title="Test", description=long_description)


def test_task_validation_priority():
    """Test that task priority is validated."""
    with pytest.raises(ValueError, match="Priority must be one of HIGH, MEDIUM, or LOW"):
        Task(id=1, title="Test", priority="INVALID_PRIORITY")


def test_task_completed_at_set_on_creation():
    """Test that completed_at is set when task is created as completed."""
    task = Task(id=1, title="Test task", completed=True)
    assert task.completed is True
    assert task.completed_at is not None