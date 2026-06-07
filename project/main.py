"""
Main script for the Task Management System.
Provides a menu-based interface for users to interact with the system.
"""

from task_manager import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress
from task_manager import validate_task_title, validate_task_description, validate_due_date
from task_manager.task_utils import display_progress, get_all_tasks

def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("TASK MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add New Task")
    print("2. Mark Task as Complete")
    print("3. View Pending Tasks")
    print("4. View Progress Report")
    print("5. View All Tasks")
    print("6. Exit")
    print("="*50)

def get_task_input():
    """Get task input from user with validation."""
    print("\n--- Add New Task ---")
    
    # Get title with validation
    while True:
        title = input("Task Title: ").strip()
        is_valid, error = validate_task_title(title)
        if is_valid:
            break
        print(f"Error: {error}")
    
    # Get description (optional)
    description = input("Task Description (optional): ").strip()
    if description:
        is_valid, error = validate_task_description(description)
        if not is_valid:
            print(f"Warning: {error}")
            description = description[:500]  # Truncate if needed
    
    # Get due date with validation
    while True:
        due_date = input("Due Date (YYYY-MM-DD): ").strip()
        is_valid, error = validate_due_date(due_date)
        if is_valid:
            break
        print(f"Error: {error}")
    
    return title, description, due_date

def add_new_task():
    """Handle adding a new task."""
    title, description, due_date = get_task_input()
    success, message, task = add_task(title, description, due_date)
    
    print(f"\n{message}")
    if success:
        print(f"Task added: {task['title']} - Due: {task['due_date']}")

def mark_task_complete():
    """Handle marking a task as complete."""
    print("\n--- Mark Task as Complete ---")
    
    # Show pending tasks first
    pending = view_pending_tasks()
    if not pending:
        print("\nNo tasks to mark as complete!")
        return
    
    task_title = input("\nEnter the title of the task to mark as complete: ").strip()
    success, message = mark_task_as_complete(task_title)
    print(f"\n{message}")

def view_all_tasks():
    """Display all tasks (both pending and completed)."""
    all_tasks = get_all_tasks()
    
    if not all_tasks:
        print("\n" + "="*50)
        print("No tasks found!")
        print("="*50)
        return
    
    print("\n" + "="*50)
    print(f"ALL TASKS ({len(all_tasks)})")
    print("="*50)
    
    pending_count = sum(1 for task in all_tasks if not task["completed"])
    completed_count = len(all_tasks) - pending_count
    
    print(f"Pending: {pending_count} | Completed: {completed_count}")
    print("-" * 50)
    
    for idx, task in enumerate(all_tasks, 1):
        status = "✓ COMPLETE" if task["completed"] else "○ PENDING"
        print(f"\n{idx}. {status}")
        print(f"   Title: {task['title']}")
        if task['description']:
            print(f"   Description: {task['description']}")
        print(f"   Due Date: {task['due_date']}")
        print("-" * 50)

def run_test_scenarios():
    """Run test scenarios to demonstrate validation."""
    print("\n" + "="*60)
    print("RUNNING TEST SCENARIOS")
    print("="*60)
    
    # Test 1: Valid task
    print("\n1. Testing valid task creation...")
    success, msg, task = add_task("Buy groceries", "Get milk and eggs", "2024-12-31")
    print(f"Result: {msg}")
    
    # Test 2: Invalid title (empty)
    print("\n2. Testing empty title...")
    success, msg, task = add_task("", "Some description", "2024-12-31")
    print(f"Result: {msg}")
    
    # Test 3: Invalid due date format
    print("\n3. Testing invalid date format...")
    success, msg, task = add_task("Valid Title", "Description", "31-12-2024")
    print(f"Result: {msg}")
    
    # Test 4: Past due date
    print("\n4. Testing past due date...")
    success, msg, task = add_task("Past Task", "This should fail", "2020-01-01")
    print(f"Result: {msg}")
    
    # Test 5: Title too long
    print("\n5. Testing title too long...")
    long_title = "A" * 150
    success, msg, task = add_task(long_title, "Description", "2025-12-31")
    print(f"Result: {msg}")

def main():
    """Main program loop."""
    print("\nWelcome to the Task Management System!")
    print("This system helps you organize and track your tasks.")
    
    # Ask if user wants to run test scenarios
    run_tests = input("\nWould you like to run test scenarios? (y/n): ").lower().strip()
    if run_tests == 'y':
        run_test_scenarios()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            add_new_task() 
        
        elif choice == '2':
            mark_task_complete()
        
        elif choice == '3':
            view_pending_tasks()
        
        elif choice == '4':
            display_progress()
        
        elif choice == '5':
            view_all_tasks()
        
        elif choice == '6':
            print("\n" + "="*50)
            print("Thank you for using the Task Management System!")
            print("Goodbye!")
            print("="*50)
            break
        
        else:
            print("\nInvalid choice! Please enter a number between 1 and 6.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()