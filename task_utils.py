from typing import List, Dict, Tuple

try:
    from .validation import validate_task_data
except (ImportError, ModuleNotFoundError):
    from validation import validate_task_data

# Global list to store tasks
tasks: List[Dict[str, object]] = []


def add_task(title: str, description: str, due_date: str) -> Tuple[bool, str, Dict[str, object] | None]:
    try:
        validate_task_data(title, description, due_date)
    except ValueError as error:
        return False, f"Validation failed: {error}", None

    task = {
        "title": title.strip(),
        "description": description.strip() if description else "",
        "due_date": due_date.strip(),
        "completed": False,
    }
    tasks.append(task)
    return True, f"Task '{task['title']}' added successfully!", task


def mark_task_as_complete(task_title: str) -> Tuple[bool, str]:
    if not isinstance(task_title, str) or len(task_title.strip()) == 0:
        return False, "Task title cannot be empty."

    normalized = task_title.strip().lower()
    for task in tasks:
        if task["title"].lower() == normalized:
            if task["completed"]:
                return False, f"Task '{task_title.strip()}' is already marked as complete."
            task["completed"] = True
            return True, f"Task '{task_title.strip()}' marked as complete!"

    return False, f"Task '{task_title.strip()}' not found."


def view_pending_tasks() -> List[Dict[str, object]]:
    pending_tasks = [task for task in tasks if not task["completed"]]
    if not pending_tasks:
        print("\n" + "=" * 50)
        print("No pending tasks found!")
        print("=" * 50)
        return pending_tasks

    print("\n" + "=" * 50)
    print(f"PENDING TASKS ({len(pending_tasks)})")
    print("=" * 50)
    for idx, task in enumerate(pending_tasks, 1):
        print(f"\n{idx}. Title: {task['title']}")
        description = task['description'] or "(No description provided)"
        print(f"   Description: {description}")
        print(f"   Due Date: {task['due_date']}")
        print(f"   Status: {'✓ Complete' if task['completed'] else '○ Pending'}")
        print("-" * 50)
    return pending_tasks


def calculate_progress(task_list=None) -> float:
    if task_list is None:
        task_list = tasks

    total_tasks = len(task_list)
    if total_tasks == 0:
        return 0.0
    completed_tasks = sum(1 for task in task_list if task["completed"])
    return (completed_tasks / total_tasks) * 100


def display_progress() -> None:
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    percentage = calculate_progress()

    print("\n" + "=" * 50)
    print("PROGRESS REPORT")
    print("=" * 50)
    print(f"Total Tasks: {total}")
    print(f"Completed Tasks: {completed}")
    print(f"Progress: {percentage:.1f}%")

    if total > 0:
        bar_length = 30
        filled_length = int(bar_length * percentage / 100)
        bar = "█" * filled_length + "░" * (bar_length - filled_length)
        print(f"Progress Bar: [{bar}]")

    if total == 0:
        print("No tasks added yet.")
    elif completed == total:
        print("Excellent! All tasks completed!")
    elif percentage >= 70:
        print("Good progress! Keep going.")
    elif percentage > 0:
        print("Making progress.")
    else:
        print("No tasks completed yet. Keep going!")

    print("=" * 50)


def get_all_tasks() -> List[Dict[str, object]]:
    return tasks.copy()


def clear_all_tasks() -> None:
    global tasks
    tasks = []
