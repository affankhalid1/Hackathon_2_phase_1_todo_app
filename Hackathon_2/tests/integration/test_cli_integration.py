"""
Integration tests for the CLI functionality of the Console Todo Application.
"""
from src.todo_app.models.task import Task, Priority
from src.todo_app.services.task_service import TaskService
from src.todo_app.cli.menu import TodoMenu
from src.todo_app.utils.formatters import format_task_list, format_single_task


def test_full_workflow_integration():
    """Test the full workflow of the application."""
    # Initialize service
    service = TaskService()

    # Add tasks
    task1 = service.add_task("Complete project proposal",
                             description="Write and review the project proposal document",
                             priority=Priority.HIGH,
                             tags=["work", "urgent"])

    task2 = service.add_task("Buy groceries",
                             description="Get milk, bread, and eggs",
                             priority=Priority.MEDIUM,
                             tags=["personal"])

    task3 = service.add_task("Schedule team meeting",
                             description="Schedule team sync for next week",
                             priority=Priority.LOW,
                             tags=["work"])

    # Verify tasks were added
    all_tasks = service.get_all_tasks()
    assert len(all_tasks) == 3

    # Test search functionality
    search_results = service.search_tasks("project")
    assert len(search_results) == 1
    assert search_results[0].title == "Complete project proposal"

    # Test filter functionality
    high_priority_tasks = service.filter_tasks(priority=Priority.HIGH)
    assert len(high_priority_tasks) == 1
    assert high_priority_tasks[0].priority == Priority.HIGH

    work_tasks = service.filter_tasks(tags=["work"])
    assert len(work_tasks) == 2
    for task in work_tasks:
        assert "work" in task.tags

    # Test update functionality
    success = service.update_task(task2.id, description="Get milk, bread, eggs, and fruit")
    assert success is True
    updated_task = service.get_task_by_id(task2.id)
    assert updated_task.description == "Get milk, bread, eggs, and fruit"

    # Test completion functionality
    success = service.mark_task_complete(task1.id, completed=True)
    assert success is True
    completed_task = service.get_task_by_id(task1.id)
    assert completed_task.completed is True
    assert completed_task.completed_at is not None

    # Test sorting functionality
    sorted_by_priority = service.sort_tasks("priority", ascending=True)  # High first
    assert sorted_by_priority[0].priority == Priority.HIGH  # High priority first

    sorted_by_title = service.sort_tasks("title", ascending=True)
    titles = [task.title for task in sorted_by_title]
    assert titles == sorted(titles)  # Should be in alphabetical order

    # Test formatting utilities
    formatted_list = format_task_list(all_tasks)
    assert "Complete project proposal" in formatted_list
    assert "Buy groceries" in formatted_list

    single_task_formatted = format_single_task(task1)
    assert str(task1.id) in single_task_formatted
    assert task1.title in single_task_formatted

    print("All integration tests passed!")


def test_edge_case_workflow():
    """Test edge cases in the workflow."""
    service = TaskService()

    # Test with empty service
    empty_tasks = service.get_all_tasks()
    assert empty_tasks == []

    search_empty = service.search_tasks("nonexistent")
    assert search_empty == []

    # Add and immediately delete
    task = service.add_task("Temporary task")
    assert len(service.get_all_tasks()) == 1

    delete_success = service.delete_task(task.id)
    assert delete_success is True
    assert len(service.get_all_tasks()) == 0
    assert service.get_task_by_id(task.id) is None

    # Test marking non-existent task
    mark_success = service.mark_task_complete(999, completed=True)
    assert mark_success is False

    # Test updating non-existent task
    update_success = service.update_task(999, title="Updated")
    assert update_success is False

    print("All edge case tests passed!")


if __name__ == "__main__":
    test_full_workflow_integration()
    test_edge_case_workflow()
    print("All integration tests completed successfully!")