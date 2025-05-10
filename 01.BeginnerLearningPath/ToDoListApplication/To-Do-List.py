import json
import os
import sys
from datetime import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file if it exists"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.tasks = json.load(file)
                print(f"Loaded {len(self.tasks)} tasks from file.")
            except json.JSONDecodeError:
                print("Error reading tasks file. Starting with empty list.")
                self.tasks = []
            except Exception as e:
                print(f"Error loading tasks: {e}")
                self.tasks = []
        else:
            self.tasks = []
    
    def save_tasks(self):
        """Save tasks to file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.tasks, file, indent=2)
            print("Tasks saved successfully!")
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self):
        """Add a new task to the list"""
        print("\n=== Add New Task ===")
        description = input("Enter task description: ").strip()
        
        if not description:
            print("Task description cannot be empty!")
            return
        
        # Optional: Add due date
        due_date = input("Enter due date (YYYY-MM-DD) or press Enter to skip: ").strip()
        if due_date:
            try:
                # Validate date format
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Task will be created without due date.")
                due_date = None
        else:
            due_date = None
        
        # Optional: Add priority
        print("Select priority level:")
        print("1. High")
        print("2. Medium")
        print("3. Low")
        priority_choice = input("Enter choice (1-3) or press Enter for medium: ").strip()
        
        priority_map = {"1": "High", "2": "Medium", "3": "Low"}
        priority = priority_map.get(priority_choice, "Medium")
        
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "due_date": due_date,
            "priority": priority
        }
        
        self.tasks.append(task)
        self.save_tasks()
        print(f'Task "{description}" added successfully!')
    
    def view_tasks(self, filter_completed=None):
        """Display all tasks or filtered tasks"""
        print("\n=== Your Current Tasks ===")
        
        if not self.tasks:
            print("No tasks found. Start by adding a new task!")
            return
        
        # Filter tasks if needed
        display_tasks = self.tasks
        if filter_completed is not None:
            display_tasks = [task for task in self.tasks if task["completed"] == filter_completed]
        
        if not display_tasks:
            status = "completed" if filter_completed else "incomplete"
            print(f"No {status} tasks found.")
            return
        
        # Sort tasks by priority
        priority_order = {"High": 0, "Medium": 1, "Low": 2}
        display_tasks.sort(key=lambda x: priority_order.get(x.get("priority", "Medium"), 1))
        
        print(f"{'ID':<4} {'Description':<30} {'Status':<12} {'Priority':<8} {'Due Date':<12}")
        print("-" * 75)
        
        for task in display_tasks:
            status = "Completed" if task["completed"] else "Incomplete"
            due_date = task.get("due_date", "Not set")
            priority = task.get("priority", "Medium")
            
            # Highlight overdue tasks
            if due_date != "Not set" and not task["completed"]:
                try:
                    if datetime.strptime(due_date, "%Y-%m-%d").date() < datetime.now().date():
                        due_date += " (OVERDUE)"
                except:
                    pass
            
            print(f"{task['id']:<4} {task['description'][:30]:<30} {status:<12} {priority:<8} {due_date:<12}")
    
    def mark_task_completed(self):
        """Mark a task as completed"""
        print("\n=== Mark Task as Completed ===")
        
        if not self.tasks:
            print("No tasks available to mark as completed.")
            return
        
        self.view_tasks(filter_completed=False)
        
        try:
            task_id = int(input("\nEnter task ID to mark as completed: "))
            
            task_found = False
            for task in self.tasks:
                if task["id"] == task_id:
                    if task["completed"]:
                        print(f'Task "{task["description"]}" is already completed!')
                    else:
                        task["completed"] = True
                        task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        self.save_tasks()
                        print(f'Task "{task["description"]}" marked as completed!')
                    task_found = True
                    break
            
            if not task_found:
                print(f"Task with ID {task_id} not found.")
        
        except ValueError:
            print("Invalid input! Please enter a valid task ID.")
    
    def delete_task(self):
        """Delete a task from the list"""
        print("\n=== Delete Task ===")
        
        if not self.tasks:
            print("No tasks available to delete.")
            return
        
        self.view_tasks()
        
        try:
            task_id = int(input("\nEnter task ID to delete: "))
            
            task_found = False
            for i, task in enumerate(self.tasks):
                if task["id"] == task_id:
                    deleted_task = self.tasks.pop(i)
                    self.save_tasks()
                    print(f'Task "{deleted_task["description"]}" deleted successfully!')
                    task_found = True
                    break
            
            if not task_found:
                print(f"Task with ID {task_id} not found.")
        
        except ValueError:
            print("Invalid input! Please enter a valid task ID.")
    
    def search_tasks(self):
        """Search for tasks by keyword"""
        print("\n=== Search Tasks ===")
        keyword = input("Enter search keyword: ").strip().lower()
        
        if not keyword:
            print("Search keyword cannot be empty!")
            return
        
        matching_tasks = [
            task for task in self.tasks 
            if keyword in task["description"].lower()
        ]
        
        if not matching_tasks:
            print(f"No tasks found containing '{keyword}'.")
            return
        
        print(f"\nFound {len(matching_tasks)} task(s) containing '{keyword}':")
        print(f"{'ID':<4} {'Description':<30} {'Status':<12} {'Priority':<8}")
        print("-" * 60)
        
        for task in matching_tasks:
            status = "Completed" if task["completed"] else "Incomplete"
            priority = task.get("priority", "Medium")
            print(f"{task['id']:<4} {task['description'][:30]:<30} {status:<12} {priority:<8}")
    
    def show_today_tasks(self):
        """Show tasks due today"""
        print("\n=== Tasks Due Today ===")
        today = datetime.now().strftime("%Y-%m-%d")
        
        today_tasks = [
            task for task in self.tasks 
            if task.get("due_date") == today and not task["completed"]
        ]
        
        if not today_tasks:
            print("No tasks due today!")
            return
        
        print(f"You have {len(today_tasks)} task(s) due today:")
        print(f"{'ID':<4} {'Description':<30} {'Priority':<8}")
        print("-" * 45)
        
        for task in today_tasks:
            priority = task.get("priority", "Medium")
            print(f"{task['id']:<4} {task['description'][:30]:<30} {priority:<8}")
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "=" * 40)
        print("    To-Do List Application")
        print("=" * 40)
        print("1. Add a Task")
        print("2. View All Tasks")
        print("3. View Incomplete Tasks")
        print("4. View Completed Tasks")
        print("5. Mark Task as Completed")
        print("6. Delete a Task")
        print("7. Search Tasks")
        print("8. View Today's Tasks")
        print("9. Exit")
        print("=" * 40)

def main():
    """Main function to run the To-Do List application"""
    todo_list = ToDoList()
    
    print("Welcome to your To-Do List Application!")
    
    while True:
        todo_list.display_menu()
        
        choice = input("Enter your choice (1-9): ").strip()
        
        if choice == "1":
            todo_list.add_task()
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks(filter_completed=False)
        elif choice == "4":
            todo_list.view_tasks(filter_completed=True)
        elif choice == "5":
            todo_list.mark_task_completed()
        elif choice == "6":
            todo_list.delete_task()
        elif choice == "7":
            todo_list.search_tasks()
        elif choice == "8":
            todo_list.show_today_tasks()
        elif choice == "9":
            print("\nThank you for using the To-Do List Application!")
            print("Your tasks have been saved. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice! Please enter a number between 1 and 9.")
        
        # Ask if user wants to continue
        while True:
            continue_choice = input("\nWould you like to perform another action? (y/n): ").lower()
            if continue_choice in ['y', 'n']:
                break
            print("Please enter 'y' or 'n'.")
        
        if continue_choice == 'n':
            print("\nThank you for using the To-Do List Application!")
            print("Your tasks have been saved. Goodbye!")
            break

if __name__ == "__main__":
    main()