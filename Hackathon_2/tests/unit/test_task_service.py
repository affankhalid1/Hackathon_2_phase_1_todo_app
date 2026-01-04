"""
Unit tests for the TaskService in the Console Todo Application.
"""
from datetime import date
from src.todo_app.models.task import Task, Priority
from src.todo_app.services.task_service import TaskService


def test_add_task():
    """Test adding a task to the service."""
    service = TaskService()
    task = service.add_task("Test task")

    assert task.id == 1
    assert task.title == "Test task"
    assert task.completed is False
    assert task.priority == Priority.MEDIUM
    assert len(service.tasks) == 1
    assert service.tasks[1] == task


def test_add_task_with_all_fields():
    """Test adding a task with all fields."""
    service = TaskService()
    test_date = date(2026, 12, 31)
    task = service.add_task(
        title="Test task",
        description="Test description",
        due_date=test_date,
        priority=Priority.HIGH,
        tags=["work", "urgent"]
    )

    assert task.title == "Test task"
    assert task.description == "Test description"
    assert task.due_date == test_date
    assert task.priority == Priority.HIGH
    assert "work" in task.tags
    assert "urgent" in task.tags


def test_get_all_tasks():
    """Test getting all tasks."""
    service = TaskService()
    service.add_task("Task 1")
    service.add_task("Task 2")

    tasks = service.get_all_tasks()

    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"


def test_get_task_by_id():
    """Test getting a task by ID."""
    service = TaskService()
    task = service.add_task("Test task")

    retrieved_task = service.get_task_by_id(task.id)

    assert retrieved_task is not None
    assert retrieved_task.id == task.id
    assert retrieved_task.title == "Test task"


def test_get_task_by_id_not_found():
    """Test getting a task that doesn't exist."""
    service = TaskService()

    retrieved_task = service.get_task_by_id(999)

    assert retrieved_task is None


def test_add_multiple_tasks():
    """Test that multiple tasks get different IDs."""
    service = TaskService()
    task1 = service.add_task("Task 1")
    task2 = service.add_task("Task 2")

    assert task1.id == 1
    assert task2.id == 2
    assert task1.id != task2.id


def test_update_task():
    """Test updating a task."""
    service = TaskService()
    original_task = service.add_task("Original task")

    success = service.update_task(original_task.id, title="Updated task", description="Updated description")

    assert success is True
    updated_task = service.get_task_by_id(original_task.id)
    assert updated_task.title == "Updated task"
    assert updated_task.description == "Updated description"


def test_update_task_not_found():
    """Test updating a task that doesn't exist."""
    service = TaskService()

    success = service.update_task(999, title="Updated task")

    assert success is False


def test_delete_task():
    """Test deleting a task."""
    service = TaskService()
    task = service.add_task("Task to delete")

    success = service.delete_task(task.id)

    assert success is True
    assert service.get_task_by_id(task.id) is None
    assert len(service.tasks) == 0


def test_delete_task_not_found():
    """Test deleting a task that doesn't exist."""
    service = TaskService()

    success = service.delete_task(999)

    assert success is False


def test_get_task_by_id():
    """Test getting a task by ID."""
    service = TaskService()
    original_task = service.add_task("Test task")

    retrieved_task = service.get_task_by_id(original_task.id)

    assert retrieved_task is not None
    assert retrieved_task.id == original_task.id
    assert retrieved_task.title == "Test task"


def test_get_task_by_id_not_found():
    """Test getting a task that doesn't exist."""
    service = TaskService()

    retrieved_task = service.get_task_by_id(999)

    assert retrieved_task is None