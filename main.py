import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

try:
    from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, display_progress, get_all_tasks
    from task_manager.validation import validate_task_title, validate_task_description, validate_due_date
except ModuleNotFoundError:
    from task_utils import add_task, mark_task_as_complete, view_pending_tasks, display_progress, get_all_tasks
    from validation import validate_task_title, validate_task_description, validate_due_date


def display_menu():
    print("\n" + "=" * 50)
    print("TASK MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add New Task")
    print("2. Mark Task as Complete")
    print("3. View Pending Tasks")
    print("4. View Progress Report")
    print("5. View All Tasks")
    print("6. Exit")
    print("=" * 50)


def get_task_input():
    while True:
        title = input("Task Title: ").strip()
        try:
            validate_task_title(title)
            break
        except ValueError as error:
            print(f"Error: {error}")

    description = input("Task Description (optional): ").strip()
    if description:
        try:
            validate_task_description(description)
        except ValueError as error:
            print(f"Warning: {error}")
            description = description[:500]

    while True:
        due_date = input("Due Date (YYYY-MM-DD): ").strip()
        try:
            validate_due_date(due_date)
            break
        except ValueError as error:
            print(f"Error: {error}")

    return title, description, due_date


def add_new_task():
    print("\n--- Add New Task ---")
    title, description, due_date = get_task_input()
    success, message, task = add_task(title, description, due_date)
    print(f"\n{message}")
    if success:
        print(f"Task added: {task['title']} - Due: {task['due_date']}")


def mark_task_complete():
    print("\n--- Mark Task as Complete ---")
    pending = view_pending_tasks()
    if not pending:
        return
    task_title = input("\nEnter the title of the task to mark as complete: ").strip()
    success, message = mark_task_as_complete(task_title)
    print(f"\n{message}")


def view_all_tasks():
    all_tasks = get_all_tasks()
    if not all_tasks:
        print("\n" + "=" * 50)
        print("No tasks found!")
        print("=" * 50)
        return

    print("\n" + "=" * 50)
    print(f"ALL TASKS ({len(all_tasks)})")
    print("=" * 50)
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
    print("\n" + "=" * 60)
    print("RUNNING TEST SCENARIOS")
    print("=" * 60)

    tests = [
        ("Buy groceries", "Get milk and eggs", "2099-12-31"),
        ("", "Some description", "2099-12-31"),
        ("Valid Title", "Description", "31-12-2024"),
        ("Past Task", "This should fail", "2000-01-01"),
        ("A" * 150, "Description", "2099-12-31"),
    ]

    for idx, (title, description, due_date) in enumerate(tests, 1):
        success, message, task = add_task(title, description, due_date)
        print(f"\n{idx}. {title[:25]}... -> {message}")


def main():
    print("\nWelcome to the Task Management System!")
    print("This system helps you organize and track your tasks.")

    while True:
        display_menu()
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
        except EOFError:
            break
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
            print("\n" + "=" * 50)
            print("Thank you for using the Task Management System!")
            print("Goodbye!")
            print("=" * 50)
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
