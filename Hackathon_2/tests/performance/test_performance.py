"""
Performance tests for the Console Todo Application.
"""
import time
import pytest
from datetime import date
from src.todo_app.models.task import Priority
from src.todo_app.services.task_service import TaskService


def test_performance_with_large_task_list():
    """Test performance with 1000+ tasks."""
    service = TaskService()

    # Add 1000 tasks
    start_time = time.time()
    for i in range(1000):
        service.add_task(
            f"Task {i}",
            description=f"Description for task {i}",
            due_date=date(2026, 1, 15) if i % 2 == 0 else None,
            priority=Priority.HIGH if i % 3 == 0 else (Priority.MEDIUM if i % 3 == 1 else Priority.LOW),
            tags=[f"tag{i % 5}", f"category{i % 3}"] if i % 10 == 0 else []
        )
    add_time = time.time() - start_time

    # Verify all tasks were added
    all_tasks = service.get_all_tasks()
    assert len(all_tasks) == 1000

    # Test that adding tasks took less than 1 second
    assert add_time < 1.0, f"Adding 1000 tasks took {add_time:.2f} seconds, which is too slow"

    # Test search performance
    start_time = time.time()
    search_results = service.search_tasks("Task 500")  # Search for specific task
    search_time = time.time() - start_time

    assert len(search_results) >= 1  # Should find at least one match
    assert search_time < 0.5, f"Searching in 1000 tasks took {search_time:.2f} seconds, which is too slow"

    # Test filter performance
    start_time = time.time()
    filter_results = service.filter_tasks(status=None, priority=Priority.HIGH)
    filter_time = time.time() - start_time

    assert filter_time < 0.5, f"Filtering 1000 tasks took {filter_time:.2f} seconds, which is too slow"

    # Test sort performance
    start_time = time.time()
    sorted_tasks = service.sort_tasks("id", ascending=True)
    sort_time = time.time() - start_time

    assert len(sorted_tasks) == 1000
    assert sort_time < 0.5, f"Sorting 1000 tasks took {sort_time:.2f} seconds, which is too slow"

    # Test update performance
    start_time = time.time()
    success = service.update_task(500, title="Updated Task 500")
    update_time = time.time() - start_time

    assert success is True
    updated_task = service.get_task_by_id(500)
    assert updated_task.title == "Updated Task 500"
    assert update_time < 0.1, f"Updating a task in 1000 tasks took {update_time:.2f} seconds, which is too slow"

    # Test delete performance
    start_time = time.time()
    success = service.delete_task(500)
    delete_time = time.time() - start_time

    assert success is True
    assert service.get_task_by_id(500) is None
    assert delete_time < 0.1, f"Deleting a task in 1000 tasks took {delete_time:.2f} seconds, which is too slow"


def test_performance_scalability():
    """Test performance scalability with different task counts."""
    task_counts = [100, 500, 1000]

    for count in task_counts:
        service = TaskService()

        # Add tasks
        start_time = time.time()
        for i in range(count):
            service.add_task(f"Task {i}")
        add_time = time.time() - start_time

        # Perform operations
        start_time = time.time()
        all_tasks = service.get_all_tasks()
        get_all_time = time.time() - start_time

        start_time = time.time()
        search_results = service.search_tasks(f"Task {count//2}")
        search_time = time.time() - start_time

        # Verify
        assert len(all_tasks) == count
        assert add_time < 2.0  # Should be under 2 seconds even for 1000 tasks
        assert get_all_time < 0.5  # Should be under 0.5 seconds
        assert search_time < 0.5  # Should be under 0.5 seconds


if __name__ == "__main__":
    test_performance_with_large_task_list()
    test_performance_scalability()
    print("All performance tests passed!")