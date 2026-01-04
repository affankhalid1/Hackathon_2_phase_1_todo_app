"""
Unit tests for search and filter functionality in the Console Todo Application.
"""
from datetime import date
from src.todo_app.models.task import Task, Priority
from src.todo_app.services.task_service import TaskService


def test_search_tasks_by_title():
    """Test searching tasks by title."""
    service = TaskService()
    service.add_task("Buy groceries", description="Get food for the week")
    service.add_task("Walk the dog", description="Take Max for a walk")
    service.add_task("Finish report", description="Complete monthly report")

    results = service.search_tasks("dog")

    assert len(results) == 1
    assert results[0].title == "Walk the dog"


def test_search_tasks_by_description():
    """Test searching tasks by description."""
    service = TaskService()
    service.add_task("Task 1", description="This is about groceries")
    service.add_task("Task 2", description="Walk the dog today")
    service.add_task("Task 3", description="Finish the report")

    results = service.search_tasks("groceries")

    assert len(results) == 1
    assert results[0].description == "This is about groceries"


def test_search_tasks_no_matches():
    """Test searching for tasks that don't exist."""
    service = TaskService()
    service.add_task("Task 1", description="This is a test")

    results = service.search_tasks("nonexistent")

    assert len(results) == 0


def test_filter_tasks_by_status():
    """Test filtering tasks by completion status."""
    service = TaskService()
    service.add_task("Pending task")
    completed_task = service.add_task("Completed task")
    service.mark_task_complete(completed_task.id)

    # Filter for completed tasks
    completed_results = service.filter_tasks(status=True)
    assert len(completed_results) == 1
    assert completed_results[0].completed is True

    # Filter for pending tasks
    pending_results = service.filter_tasks(status=False)
    assert len(pending_results) == 1
    assert pending_results[0].completed is False


def test_filter_tasks_by_priority():
    """Test filtering tasks by priority."""
    service = TaskService()
    service.add_task("Low priority task", priority=Priority.LOW)
    service.add_task("High priority task", priority=Priority.HIGH)
    service.add_task("Medium priority task", priority=Priority.MEDIUM)

    # Filter for high priority
    high_priority_results = service.filter_tasks(priority=Priority.HIGH)
    assert len(high_priority_results) == 1
    assert high_priority_results[0].priority == Priority.HIGH


def test_filter_tasks_by_tags():
    """Test filtering tasks by tags."""
    service = TaskService()
    service.add_task("Task 1", tags=["work", "urgent"])
    service.add_task("Task 2", tags=["personal"])
    service.add_task("Task 3", tags=["work", "low-priority"])

    # Filter for tasks with "work" tag
    work_results = service.filter_tasks(tags=["work"])
    assert len(work_results) == 2  # Should match both tasks with "work" tag
    for task in work_results:
        assert "work" in task.tags


def test_filter_tasks_by_due_date_overdue():
    """Test filtering tasks by due date - overdue."""
    service = TaskService()
    past_date = date(2020, 1, 1)  # Past date
    future_date = date(2030, 1, 1)  # Future date

    service.add_task("Overdue task", due_date=past_date)
    service.add_task("Future task", due_date=future_date)

    overdue_results = service.filter_tasks(due_date_filter="overdue")
    assert len(overdue_results) == 1
    assert overdue_results[0].due_date == past_date


def test_filter_tasks_no_filters():
    """Test filtering with no filters (should return all tasks)."""
    service = TaskService()
    service.add_task("Task 1")
    service.add_task("Task 2")

    all_results = service.filter_tasks()
    assert len(all_results) == 2