# Quickstart Guide: Console Todo Application

## Overview
This guide provides a quick introduction to setting up and using the Console Todo Application. The application is a command-line tool for managing tasks with features like adding, viewing, updating, deleting, searching, filtering, and sorting.

## Prerequisites
- Python 3.12 or higher
- No external dependencies required (uses only Python standard library)

## Installation
1. Clone or download the repository containing the application
2. Navigate to the project directory in your terminal
3. The application is ready to use (no installation required)

## Running the Application
To run the application, execute:
```bash
python -m src.todo_app.main
```

Or if the main.py file is in the current directory:
```bash
python src/todo_app/main.py
```

## Basic Usage
When the application starts, you'll see a menu with the following options:

1. **Add Task**: Create a new task with title, description, due date, priority, and tags
2. **View All Tasks**: Display all tasks in a formatted list
3. **Update Task**: Modify an existing task by ID
4. **Delete Task**: Remove a task by ID with confirmation
5. **Mark Complete**: Toggle task completion status
6. **Search Tasks**: Find tasks by keyword in title or description
7. **Filter Tasks**: Filter tasks by status, priority, tags, or due date
8. **Sort Tasks**: Sort tasks by due date, priority, title, or creation date
9. **Exit**: Quit the application

## Example Workflow
1. Start the application
2. Choose option 1 to add a task:
   - Enter a title (required)
   - Enter a description (optional)
   - Enter due date in YYYY-MM-DD format (optional)
   - Select priority (High/Medium/Low)
   - Enter tags as comma-separated values (optional)
3. Choose option 2 to view all tasks
4. Choose option 3 to update a task by its ID
5. Choose option 5 to mark a task as complete/incomplete

## Key Features
- **In-Memory Storage**: All tasks are stored in memory and persist only during runtime
- **Validation**: Input is validated for correct format and required fields
- **Confirmation Prompts**: Critical operations like deletion require confirmation
- **Flexible Search**: Search across title and description fields
- **Multiple Filters**: Filter by status, priority, tags, and due date
- **Sorting Options**: Sort tasks by various criteria
- **Intuitive Menu**: Easy navigation with numbered options

## Exiting
To exit the application, select option 9 from the main menu or use Ctrl+C to terminate the process.

## Troubleshooting
- If you get a "module not found" error, ensure you're running Python from the project root directory
- If dates aren't accepted, ensure they're in the format YYYY-MM-DD (e.g., 2026-12-31)
- If you enter invalid input, the application will prompt you again with proper guidance