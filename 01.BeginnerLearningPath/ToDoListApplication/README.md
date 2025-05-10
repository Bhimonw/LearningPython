# To-Do List Application

A feature-rich console-based To-Do List application built with Python. This application helps users manage their daily tasks with features like due dates, priorities, and persistent storage.

## Features

### Core Features
- **Add Tasks**: Create new tasks with descriptions
- **View Tasks**: Display all tasks with their status
- **Mark Complete**: Mark tasks as completed
- **Delete Tasks**: Remove tasks from the list
- **Persistent Storage**: Tasks are saved automatically to a JSON file

### Enhanced Features
- **Due Dates**: Set due dates for tasks with overdue notifications
- **Priority Levels**: Assign High, Medium, or Low priority to tasks
- **Task Filtering**: View only completed or incomplete tasks
- **Search Function**: Find tasks by keyword
- **Today's Tasks**: View tasks due today
- **Task IDs**: Unique identifiers for easy task management
- **Timestamps**: Track when tasks were created and completed

## Installation

1. Ensure you have Python 3.x installed on your system
2. Clone or download this repository:
   ```bash
   git clone https://github.com/yourusername/todo-list-app.git
   cd todo-list-app
   ```
3. No external dependencies required!

## Usage

Run the application:
```bash
python todo_list_app.py
```

### Menu Options

1. **Add a Task**: Create a new task with optional due date and priority
2. **View All Tasks**: Display all tasks sorted by priority
3. **View Incomplete Tasks**: Show only pending tasks
4. **View Completed Tasks**: Show only finished tasks
5. **Mark Task as Completed**: Update a task's status to complete
6. **Delete a Task**: Remove a task from the list
7. **Search Tasks**: Find tasks containing specific keywords
8. **View Today's Tasks**: Display tasks due today
9. **Exit**: Save and close the application

## Example Usage

```
Welcome to your To-Do List Application!

========================================
    To-Do List Application
========================================
1. Add a Task
2. View All Tasks
3. View Incomplete Tasks
4. View Completed Tasks
5. Mark Task as Completed
6. Delete a Task
7. Search Tasks
8. View Today's Tasks
9. Exit
========================================
Enter your choice (1-9): 1

=== Add New Task ===
Enter task description: Finish project documentation
Enter due date (YYYY-MM-DD) or press Enter to skip: 2025-05-15
Select priority level:
1. High
2. Medium
3. Low
Enter choice (1-3) or press Enter for medium: 1
Task "Finish project documentation" added successfully!

Would you like to perform another action? (y/n): y

========================================
    To-Do List Application
========================================
[Menu options...]
Enter your choice (1-9): 2

=== Your Current Tasks ===
ID   Description                    Status       Priority Due Date    
---------------------------------------------------------------------------
1    Finish project documentation   Incomplete   High     2025-05-15  
```

## Data Storage

Tasks are stored in a JSON file (`tasks.json`) in the same directory as the application. This file is automatically created and updated whenever tasks are modified.

### Task Structure

Each task contains:
- `id`: Unique identifier
- `description`: Task description
- `completed`: Boolean status
- `created_at`: Creation timestamp
- `due_date`: Optional due date
- `priority`: Task priority (High/Medium/Low)
- `completed_at`: Completion timestamp (when applicable)

## Key Concepts Demonstrated

1. **Object-Oriented Programming**: Uses a `ToDoList` class to encapsulate functionality
2. **File Handling**: JSON file operations for data persistence
3. **Error Handling**: Graceful handling of invalid inputs and file errors
4. **Data Structures**: Lists and dictionaries for task management
5. **Control Flow**: Loops, conditionals, and function calls
6. **User Input Validation**: Ensures valid data entry
7. **Datetime Operations**: Working with dates and timestamps

## Code Structure

- `ToDoList` class: Core application logic
  - `load_tasks()`: Load tasks from file
  - `save_tasks()`: Save tasks to file
  - `add_task()`: Create new tasks
  - `view_tasks()`: Display tasks with filtering
  - `mark_task_completed()`: Update task status
  - `delete_task()`: Remove tasks
  - `search_tasks()`: Find tasks by keyword
  - `show_today_tasks()`: Filter tasks due today
  - `display_menu()`: Show user interface

## Future Enhancements

Potential improvements for future versions:
- GUI interface using tkinter or PyQt
- Task categories or tags
- Recurring tasks
- Task reminders/notifications
- Export tasks to CSV/PDF
- Multi-user support
- Cloud synchronization
- Task statistics and analytics
- Backup and restore functionality
- Task dependencies
- Subtasks support

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by productivity applications and task management systems
- Built as an educational project for Python beginners
- Designed to demonstrate practical Python programming concepts

## Troubleshooting

### Common Issues

1. **Tasks not saving**: Ensure you have write permissions in the application directory
2. **Date format errors**: Use YYYY-MM-DD format for dates
3. **File corruption**: Delete `tasks.json` to start fresh if the file becomes corrupted

### Support

For issues or questions, please open an issue on the GitHub repository or contact the maintainer.