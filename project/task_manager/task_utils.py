"""
Task utilities module for task management system.
Contains functions for task operations like adding, completing, viewing, and tracking progress.
"""

from .validation import validate_task_title, validate_task_description, validate_due_date, validate_task_data

# Global list to store tasks
tasks = []

def add_task(title, description, due_date):
    """
    Add a new task to the task list after validation.
    
    Args:
        title (str): Task title
        description (str): Task description
        due_date (str): Task due date in YYYY-MM-DD format
        
    Returns:
        tuple: (success, message, task_dict)
    """
    # Validate all inputs
    is_valid, errors = validate_task_data(title, description, due_date)
    
    if not is_valid:
        error_message = "; ".join(errors)
        return False, f"Validation failed: {error_message}", None
    
    # Create task dictionary
    task = {
        "title": title.strip(),
        "description": description.strip() if description else "",
        "due_date": due_date.strip(),
        "completed": False
    }
    
    # Add to tasks list
    tasks.append(task)
    return True, f"Task '{task['title']}' added successfully!", task

def mark_task_as_complete(task_title):
    """
    Mark a task as complete by its title.
    
    Args:
        task_title (str): The title of the task to mark as complete
        
    Returns:
        tuple: (success, message)
    """
    if not task_title or not isinstance(task_title, str):
        return False, "Task title cannot be empty."
    
    task_title = task_title.strip()
    
    # Search for the task
    for task in tasks:
        if task["title"].lower() == task_title.lower():
            if task["completed"]:
                return False, f"Task '{task_title}' is already marked as complete."
            task["completed"] = True
            return True, f"Task '{task_title}' marked as complete!"
    
    return False, f"Task '{task_title}' not found."

def view_pending_tasks():
    """
    View all pending (incomplete) tasks.
    
    Returns:
        list: List of pending tasks
    """
    pending_tasks = [task for task in tasks if not task["completed"]]
    
    if not pending_tasks:
        print("\n" + "="*50)
        print("No pending tasks found!")
        print("="*50)
        return pending_tasks
    
    print("\n" + "="*50)
    print(f"PENDING TASKS ({len(pending_tasks)})")
    print("="*50)
    
    for idx, task in enumerate(pending_tasks, 1):
        print(f"\n{idx}. Title: {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Due Date: {task['due_date']}")
        print(f"   Status: {'✓ Complete' if task['completed'] else '○ Pending'}")
        print("-" * 50)
    
    return pending_tasks

def calculate_progress():
    """
    Calculate the progress of task completion.
    
    Returns:
        tuple: (total_tasks, completed_tasks, percentage, status_summary)
    """
    total_tasks = len(tasks)
    
    if total_tasks == 0:
        return 0, 0, 0.0, "No tasks added yet."
    
    completed_tasks = sum(1 for task in tasks if task["completed"])
    percentage = (completed_tasks / total_tasks) * 100
    
    # Create status summary
    if percentage == 100:
        status_summary = "Excellent! All tasks completed!"
    elif percentage >= 70:
        status_summary = f"Good progress! {percentage:.1f}% completed."
    elif percentage >= 40:
        status_summary = f"Making progress. {percentage:.1f}% completed."
    elif percentage > 0:
        status_summary = f"Getting started. {percentage:.1f}% completed."
    else:
        status_summary = "No tasks completed yet. Keep going!"
    
    return total_tasks, completed_tasks, percentage, status_summary

def display_progress():
    """
    Display formatted progress information.
    """
    total, completed, percentage, summary = calculate_progress()
    
    print("\n" + "="*50)
    print("PROGRESS REPORT")
    print("="*50)
    print(f"Total Tasks: {total}")
    print(f"Completed Tasks: {completed}")
    print(f"Progress: {percentage:.1f}%")
    
    # Create progress bar
    if total > 0:
        bar_length = 30
        filled_length = int(bar_length * percentage / 100)
        bar = "█" * filled_length + "░" * (bar_length - filled_length)
        print(f"Progress Bar: [{bar}]")
    
    print(f"\n{summary}")
    print("="*50)

def get_all_tasks():
    """
    Get all tasks (for display purposes).
    
    Returns:
        list: All tasks
    """
    return tasks.copy()

def clear_all_tasks():
    """
    Clear all tasks (useful for testing).
    
    Returns:
        bool: True if successful
    """
    global tasks
    tasks = []
    return True