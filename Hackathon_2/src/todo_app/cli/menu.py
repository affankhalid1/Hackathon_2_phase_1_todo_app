"""
Console Todo Application - CLI Menu

This module provides the command-line interface for the todo application.
"""
from typing import List
from ..models.task import Task, Priority
from ..services.task_service import TaskService
from ..utils.formatters import format_task_list, format_single_task
from ..utils.validators import validate_task_data
from ..utils.dates import parse_date


class TodoMenu:
    """Main menu class for the todo application CLI."""

    def __init__(self):
        """Initialize the menu with a task service."""
        self.task_service = TaskService()

    def display_menu(self):
        """Display the main menu options."""
        print("\n=== Console Todo Application ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Complete/Incomplete")
        print("6. Search Tasks")
        print("7. Filter Tasks")
        print("8. Sort Tasks")
        print("9. Exit")
        print("================================")

    def get_user_choice(self) -> str:
        """Get user choice from the menu."""
        choice = input("Enter your choice (1-9): ").strip()
        return choice

    def add_task(self):
        """Add a new task."""
        print("\n--- Add New Task ---")
        title = input("Enter task title: ").strip()

        # Validate title
        if not title:
            print("Error: Title cannot be empty")
            return

        description = input("Enter task description (optional, press Enter to skip): ").strip()
        if not description:
            description = None

        due_date_input = input("Enter due date (YYYY-MM-DD, optional, press Enter to skip): ").strip()
        due_date = parse_date(due_date_input) if due_date_input else None

        priority_input = input("Enter priority (High/Medium/Low, default: Medium): ").strip().title()
        if not priority_input:
            priority = Priority.MEDIUM
        elif priority_input.lower() == "high":
            priority = Priority.HIGH
        elif priority_input.lower() == "low":
            priority = Priority.LOW
        else:
            priority = Priority.MEDIUM

        tags_input = input("Enter tags (comma-separated, optional, press Enter to skip): ").strip()
        tags = []
        if tags_input:
            tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]

        # Validate task data
        is_valid, errors = validate_task_data(title, description, due_date_input if due_date_input else None,
                                           priority_input if priority_input else None, tags)
        if not is_valid:
            print("Validation errors:")
            for error in errors:
                print(f"- {error}")
            return

        try:
            task = self.task_service.add_task(title, description, due_date, priority, tags)
            print(f"✓ Task added successfully! (ID: {task.id})")
        except ValueError as e:
            print(f"Error: {e}")

    def view_all_tasks(self):
        """View all tasks."""
        print("\n--- All Tasks ---")
        tasks = self.task_service.get_all_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            formatted_output = format_task_list(tasks)
            print(formatted_output)

    def update_task(self):
        """Update an existing task."""
        print("\n--- Update Task ---")
        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Error: Please enter a valid task ID (number)")
            return

        task = self.task_service.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found")
            return

        print(f"Current task: {format_single_task(task)}")

        title = input(f"Enter new title (current: '{task.title}', press Enter to keep current): ").strip()
        title = title if title else task.title

        description = input(f"Enter new description (current: '{task.description}', press Enter to keep current): ").strip()
        if description == "":
            description = task.description

        due_date_input = input(f"Enter new due date (YYYY-MM-DD, current: '{task.due_date}', press Enter to keep current): ").strip()
        if due_date_input:
            from ..utils.dates import parse_date
            due_date = parse_date(due_date_input)
        else:
            due_date = task.due_date

        priority_input = input(f"Enter new priority (High/Medium/Low, current: '{task.priority.value}', press Enter to keep current): ").strip()
        if priority_input:
            priority_input = priority_input.title()
            if priority_input.lower() == "high":
                priority = Priority.HIGH
            elif priority_input.lower() == "low":
                priority = Priority.LOW
            elif priority_input.lower() == "medium":
                priority = Priority.MEDIUM
            else:
                print("Invalid priority. Keeping current priority.")
                priority = task.priority
        else:
            priority = task.priority

        tags_input = input(f"Enter new tags (comma-separated, current: '{', '.join(task.tags)}', press Enter to keep current): ").strip()
        if tags_input:
            tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
        else:
            tags = task.tags

        # Validate task data
        is_valid, errors = validate_task_data(title, description,
                                           str(due_date) if due_date else None,
                                           priority_input if priority_input else None,
                                           tags)
        if not is_valid:
            print("Validation errors:")
            for error in errors:
                print(f"- {error}")
            return

        success = self.task_service.update_task(task_id, title, description, due_date, priority, tags)
        if success:
            print("✓ Task updated successfully!")
        else:
            print("Error: Failed to update task")

    def delete_task(self):
        """Delete a task."""
        print("\n--- Delete Task ---")
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Error: Please enter a valid task ID (number)")
            return

        task = self.task_service.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found")
            return

        print(f"Task to delete: {format_single_task(task)}")
        confirm = input("Are you sure you want to delete this task? (y/N): ").strip().lower()
        if confirm in ['y', 'yes']:
            success = self.task_service.delete_task(task_id)
            if success:
                print("✓ Task deleted successfully!")
            else:
                print("Error: Failed to delete task")
        else:
            print("Task deletion cancelled.")

    def mark_task_complete(self):
        """Mark a task as complete or incomplete."""
        print("\n--- Mark Task Complete/Incomplete ---")
        try:
            task_id = int(input("Enter task ID: "))
        except ValueError:
            print("Error: Please enter a valid task ID (number)")
            return

        task = self.task_service.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found")
            return

        print(f"Current task: {format_single_task(task)}")
        current_status = "Complete" if task.completed else "Pending"
        new_status = "Pending" if task.completed else "Complete"
        print(f"Current status: {current_status}")
        print(f"New status: {new_status}")

        confirm = input(f"Mark task as {new_status.lower()}? (y/N): ").strip().lower()
        if confirm in ['y', 'yes']:
            success = self.task_service.mark_task_complete(task_id, not task.completed)
            if success:
                print(f"✓ Task marked as {new_status.lower()} successfully!")
            else:
                print("Error: Failed to update task status")
        else:
            print("Task status update cancelled.")

    def search_tasks(self):
        """Search tasks by keyword."""
        print("\n--- Search Tasks ---")
        keyword = input("Enter keyword to search: ").strip()
        if not keyword:
            print("Error: Keyword cannot be empty")
            return

        tasks = self.task_service.search_tasks(keyword)
        if not tasks:
            print("No matching tasks found.")
        else:
            print(f"Found {len(tasks)} matching task(s):")
            formatted_output = format_task_list(tasks)
            print(formatted_output)

    def filter_tasks(self):
        """Filter tasks by criteria."""
        print("\n--- Filter Tasks ---")
        print("Filter options:")
        print("1. By status (completed/pending)")
        print("2. By priority")
        print("3. By due date (overdue/today/this week)")
        print("4. By tags")

        filter_choice = input("Enter filter option (1-4): ").strip()
        status = priority = due_date_filter = tags = None

        if filter_choice == "1":
            status_choice = input("Enter status (completed/pending): ").strip().lower()
            if status_choice == "completed":
                status = True
            elif status_choice == "pending":
                status = False
            else:
                print("Invalid status. Use 'completed' or 'pending'.")
                return
        elif filter_choice == "2":
            priority_choice = input("Enter priority (high/medium/low): ").strip().lower()
            if priority_choice == "high":
                priority = Priority.HIGH
            elif priority_choice == "medium":
                priority = Priority.MEDIUM
            elif priority_choice == "low":
                priority = Priority.LOW
            else:
                print("Invalid priority. Use 'high', 'medium', or 'low'.")
                return
        elif filter_choice == "3":
            date_choice = input("Enter date filter (overdue/today/week): ").strip().lower()
            if date_choice in ["overdue", "today", "week"]:
                due_date_filter = date_choice
            else:
                print("Invalid date filter. Use 'overdue', 'today', or 'week'.")
                return
        elif filter_choice == "4":
            tags_input = input("Enter tags to filter by (comma-separated): ").strip()
            if tags_input:
                tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
            else:
                print("No tags provided.")
                return
        else:
            print("Invalid filter option.")
            return

        tasks = self.task_service.filter_tasks(status, priority, tags, due_date_filter)
        if not tasks:
            print("No matching tasks found.")
        else:
            print(f"Found {len(tasks)} matching task(s):")
            formatted_output = format_task_list(tasks)
            print(formatted_output)

    def sort_tasks(self):
        """Sort tasks by criteria."""
        print("\n--- Sort Tasks ---")
        print("Sort options:")
        print("1. By ID")
        print("2. By Title")
        print("3. By Due Date")
        print("4. By Priority")
        print("5. By Creation Date")

        sort_choice = input("Enter sort option (1-5): ").strip()
        sort_by = ""
        if sort_choice == "1":
            sort_by = "id"
        elif sort_choice == "2":
            sort_by = "title"
        elif sort_choice == "3":
            sort_by = "due_date"
        elif sort_choice == "4":
            sort_by = "priority"
        elif sort_choice == "5":
            sort_by = "created_at"
        else:
            print("Invalid sort option.")
            return

        order_choice = input("Sort order (asc/desc): ").strip().lower()
        ascending = order_choice != "desc"

        tasks = self.task_service.sort_tasks(sort_by, ascending)
        if not tasks:
            print("No tasks to display.")
        else:
            print(f"Tasks sorted by {sort_by} ({'ascending' if ascending else 'descending'}):")
            formatted_output = format_task_list(tasks)
            print(formatted_output)

    def run(self):
        """Run the main menu loop."""
        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_all_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.mark_task_complete()
            elif choice == "6":
                self.search_tasks()
            elif choice == "7":
                self.filter_tasks()
            elif choice == "8":
                self.sort_tasks()
            elif choice == "9":
                print("Thank you for using the Console Todo Application!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")

            # Pause before showing menu again
            input("\nPress Enter to continue...")