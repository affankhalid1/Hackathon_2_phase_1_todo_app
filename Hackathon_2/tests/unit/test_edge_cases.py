"""
Unit tests for edge cases in the Console Todo Application.
"""
import pytest
from datetime import date
from src.todo_app.models.task import Task, Priority
from src.todo_app.services.task_service import TaskService


def test_task_title_edge_cases():
    """Test edge cases for task titles."""
    service = TaskService()

    # Test with minimum length title
    short_task = service.add_task("A")  # 1 character
    assert short_task.title == "A"

    # Test with maximum length title
    long_title = "x" * 100  # 100 characters
    long_task = service.add_task(long_title)
    assert long_task.title == long_title

    # Test that title longer than 100 chars raises error
    with pytest.raises(ValueError):
        service.add_task("x" * 101)  # 101 characters


def test_task_description_edge_cases():
    """Test edge cases for task descriptions."""
    service = TaskService()

    # Test with maximum length description
    long_description = "x" * 500  # 500 characters
    task = service.add_task("Test task", description=long_description)
    assert task.description == long_description

    # Test that description longer than 500 chars raises error
    with pytest.raises(ValueError):
        service.add_task("Test", description="x" * 501)  # 501 characters


def test_task_empty_description():
    """Test task with empty string as description."""
    service = TaskService()
    task = service.add_task("Test task", description="")
    assert task.description == ""


def test_task_with_special_characters():
    """Test task with special characters in title and description."""
    service = TaskService()
    special_title = "Task with special chars: !@#$%^&*()"
    special_desc = "Description with special chars: <>{}[]|\\\"'/:;?"

    task = service.add_task(special_title, description=special_desc)
    assert task.title == special_title
    assert task.description == special_desc


def test_task_with_unicode():
    """Test task with unicode characters."""
    service = TaskService()
    unicode_title = "Task with unicode: café, naïve, résumé"
    unicode_desc = "Description with unicode: 你好, Здравствуй, مرحبا"

    task = service.add_task(unicode_title, description=unicode_desc)
    assert task.title == unicode_title
    assert task.description == unicode_desc


def test_task_priority_edge_cases():
    """Test edge cases for task priority."""
    service = TaskService()

    # Test all priority levels
    high_task = service.add_task("High task", priority=Priority.HIGH)
    medium_task = service.add_task("Medium task", priority=Priority.MEDIUM)
    low_task = service.add_task("Low task", priority=Priority.LOW)

    assert high_task.priority == Priority.HIGH
    assert medium_task.priority == Priority.MEDIUM
    assert low_task.priority == Priority.LOW


def test_task_tags_edge_cases():
    """Test edge cases for task tags."""
    service = TaskService()

    # Test with empty tags list
    task1 = service.add_task("Task 1", tags=[])
    assert task1.tags == []

    # Test with single tag
    task2 = service.add_task("Task 2", tags=["single"])
    assert task2.tags == ["single"]

    # Test with multiple tags
    tags_list = ["tag1", "tag2", "tag3"]
    task3 = service.add_task("Task 3", tags=tags_list)
    assert set(task3.tags) == set(tags_list)


def test_task_duplicate_tags():
    """Test task with duplicate tags."""
    service = TaskService()
    task = service.add_task("Test task", tags=["work", "work", "personal"])
    # Implementation should handle duplicates as needed
    assert "work" in task.tags
    assert "personal" in task.tags


def test_task_date_edge_cases():
    """Test edge cases for task due dates."""
    service = TaskService()

    # Test with past date
    past_date = date(2020, 1, 1)
    past_task = service.add_task("Past task", due_date=past_date)
    assert past_task.due_date == past_date

    # Test with future date
    future_date = date(2030, 12, 31)
    future_task = service.add_task("Future task", due_date=future_date)
    assert future_task.due_date == future_date

    # Test with today's date
    today = date.today()
    today_task = service.add_task("Today task", due_date=today)
    assert today_task.due_date == today


def test_task_without_due_date():
    """Test task without due date."""
    service = TaskService()
    task = service.add_task("No due date task")
    assert task.due_date is None


def test_task_completion_edge_cases():
    """Test edge cases for task completion."""
    service = TaskService()

    # Test task creation with completed=False by default
    task = service.add_task("Incomplete task")
    assert task.completed is False
    assert task.completed_at is None

    # Test marking task as complete
    service.mark_task_complete(task.id, completed=True)
    completed_task = service.get_task_by_id(task.id)
    assert completed_task.completed is True
    assert completed_task.completed_at is not None

    # Test marking task as incomplete
    service.mark_task_complete(task.id, completed=False)
    incomplete_task = service.get_task_by_id(task.id)
    assert incomplete_task.completed is False
    assert incomplete_task.completed_at is None


def test_task_service_empty_operations():
    """Test operations on empty task service."""
    service = TaskService()

    # Test getting all tasks when none exist
    all_tasks = service.get_all_tasks()
    assert all_tasks == []

    # Test searching when no tasks exist
    search_results = service.search_tasks("nonexistent")
    assert search_results == []

    # Test filtering when no tasks exist
    filter_results = service.filter_tasks(status=True)
    assert filter_results == []

    # Test sorting when no tasks exist
    sort_results = service.sort_tasks("id")
    assert sort_results == []


def test_task_service_large_number_of_tasks():
    """Test performance with a large number of tasks."""
    service = TaskService()

    # Add many tasks
    for i in range(50):  # Testing with 50 tasks (less than 1000 for test speed)
        service.add_task(f"Task {i}", description=f"Description for task {i}")

    all_tasks = service.get_all_tasks()
    assert len(all_tasks) == 50

    # Test search in large list
    search_results = service.search_tasks("Task 10")
    assert len(search_results) == 1
    assert search_results[0].title == "Task 10"


def test_task_update_edge_cases():
    """Test edge cases for updating tasks."""
    service = TaskService()
    original_task = service.add_task("Original", description="Original description")

    # Update with same values (should work)
    success = service.update_task(original_task.id, title="Original", description="Original description")
    assert success is True

    # Update only title
    success = service.update_task(original_task.id, title="Updated title")
    assert success is True
    updated_task = service.get_task_by_id(original_task.id)
    assert updated_task.title == "Updated title"
    assert updated_task.description == "Original description"  # Should remain unchanged

    # Update only description
    success = service.update_task(original_task.id, description="Updated description")
    assert success is True
    updated_task = service.get_task_by_id(original_task.id)
    assert updated_task.title == "Updated title"  # Should remain unchanged
    assert updated_task.description == "Updated description"


def test_task_update_nonexistent():
    """Test updating a non-existent task."""
    service = TaskService()

    success = service.update_task(999, title="Should not work")
    assert success is False


def test_task_delete_nonexistent():
    """Test deleting a non-existent task."""
    service = TaskService()

    success = service.delete_task(999)
    assert success is False


def test_task_get_nonexistent():
    """Test getting a non-existent task."""
    service = TaskService()

    task = service.get_task_by_id(999)
    assert task is None