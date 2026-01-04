"""
Unit tests for sort functionality in the Console Todo Application.
"""
from datetime import date
from src.todo_app.models.task import Task, Priority
from src.todo_app.services.task_service import TaskService


def test_sort_tasks_by_id():
    """Test sorting tasks by ID."""
    service = TaskService()
    task3 = service.add_task("Task 3")
    task1 = service.add_task("Task 1")
    task2 = service.add_task("Task 2")

    # Sort by ID ascending
    sorted_tasks = service.sort_tasks("id", ascending=True)
    assert len(sorted_tasks) == 3
    assert sorted_tasks[0].id == task1.id
    assert sorted_tasks[1].id == task2.id
    assert sorted_tasks[2].id == task3.id

    # Sort by ID descending
    sorted_tasks_desc = service.sort_tasks("id", ascending=False)
    assert sorted_tasks_desc[0].id == task3.id
    assert sorted_tasks_desc[1].id == task2.id
    assert sorted_tasks_desc[2].id == task1.id


def test_sort_tasks_by_title():
    """Test sorting tasks by title."""
    service = TaskService()
    service.add_task("Zebra task")
    service.add_task("Apple task")
    service.add_task("Mango task")

    # Sort by title ascending
    sorted_tasks = service.sort_tasks("title", ascending=True)
    assert len(sorted_tasks) == 3
    assert sorted_tasks[0].title == "Apple task"
    assert sorted_tasks[1].title == "Mango task"
    assert sorted_tasks[2].title == "Zebra task"

    # Sort by title descending
    sorted_tasks_desc = service.sort_tasks("title", ascending=False)
    assert sorted_tasks_desc[0].title == "Zebra task"
    assert sorted_tasks_desc[1].title == "Mango task"
    assert sorted_tasks_desc[2].title == "Apple task"


def test_sort_tasks_by_priority():
    """Test sorting tasks by priority."""
    service = TaskService()
    service.add_task("Low priority", priority=Priority.LOW)
    service.add_task("High priority", priority=Priority.HIGH)
    service.add_task("Medium priority", priority=Priority.MEDIUM)

    # Sort by priority ascending (High, Medium, Low)
    sorted_tasks = service.sort_tasks("priority", ascending=True)
    assert len(sorted_tasks) == 3
    assert sorted_tasks[0].priority == Priority.HIGH  # High priority first
    assert sorted_tasks[1].priority == Priority.MEDIUM
    assert sorted_tasks[2].priority == Priority.LOW

    # Sort by priority descending (Low, Medium, High)
    sorted_tasks_desc = service.sort_tasks("priority", ascending=False)
    assert sorted_tasks_desc[0].priority == Priority.LOW
    assert sorted_tasks_desc[1].priority == Priority.MEDIUM
    assert sorted_tasks_desc[2].priority == Priority.HIGH


def test_sort_tasks_by_due_date():
    """Test sorting tasks by due date."""
    service = TaskService()
    future_date = date(2030, 12, 31)
    past_date = date(2020, 1, 1)
    today_date = date.today()

    service.add_task("Future task", due_date=future_date)
    service.add_task("Past task", due_date=past_date)
    service.add_task("Today task", due_date=today_date)

    # Sort by due date ascending (earliest first)
    sorted_tasks = service.sort_tasks("due_date", ascending=True)
    assert len(sorted_tasks) == 3
    assert sorted_tasks[0].due_date == past_date  # Past date first
    assert sorted_tasks[1].due_date == today_date
    assert sorted_tasks[2].due_date == future_date

    # Sort by due date descending (latest first)
    sorted_tasks_desc = service.sort_tasks("due_date", ascending=False)
    assert sorted_tasks_desc[0].due_date == future_date  # Future date first
    assert sorted_tasks_desc[1].due_date == today_date
    assert sorted_tasks_desc[2].due_date == past_date