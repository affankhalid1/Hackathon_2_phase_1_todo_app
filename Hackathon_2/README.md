# Console Todo Application

A command-line todo list manager built in Python with an intuitive text-based interface. All data stored in memory (no database/files) with full CRUD operations, filtering, and organization features.

## Features

- **Task Management**: Add, view, update, delete tasks
- **Task Organization**: Priorities (High, Medium, Low) with visual indicators
- **Tags/Categories**: Multiple tags per task (e.g., "work", "home", "urgent")
- **Completion Status**: Toggle between pending/complete with timestamps
- **Search & Filter**: Search across title and description fields, filter by status, priority, tags, and date
- **Sorting**: Sort by due date, priority, title, or creation date

## Requirements

- Python 3.12 or higher
- Standard library only (no external dependencies)

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Run the application with Python:

```bash
python -m src.todo_app.main
```

## Usage

The application provides a menu-driven interface:

1. **Add Task**: Create tasks with title, description, due date, priority, and tags
2. **View All Tasks**: Display formatted list of all tasks with key details
3. **Update Task**: Edit any task field (title, description, due date, priority, tags)
4. **Delete Task**: Remove tasks by ID with confirmation prompt
5. **Mark Complete**: Toggle task completion status with timestamps
6. **Search Tasks**: Search across title and description fields
7. **Filter Tasks**: Filter by status, priority, tags, or date
8. **Sort Tasks**: Sort by due date, priority, title, or creation date
9. **Exit**: Quit the application

## Data Model

Each task includes:
- Unique ID (auto-generated)
- Title (required, max 100 chars)
- Description (optional, max 500 chars)
- Due date (optional, ISO format YYYY-MM-DD)
- Priority (High, Medium, Low)
- Tags (multiple allowed)
- Completion status with timestamps

## Architecture

The application follows a clean architecture pattern:

- `src/todo_app/models/` - Data models (Task, Priority)
- `src/todo_app/services/` - Business logic (TaskService)
- `src/todo_app/cli/` - User interface (menu system)
- `src/todo_app/utils/` - Utility functions (validation, formatting, dates)

## Testing

Run the unit tests using pytest:

```bash
pip install pytest
pytest tests/
```

## Performance

- All operations complete in <1 second for up to 1000 tasks
- Data stored in memory only (no persistence to files or databases)
- Console-based interface only, no GUI

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.