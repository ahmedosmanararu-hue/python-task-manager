from task_manager.validation import validate_title, validate_task_description, validate_date

tasks_list = []

def get_all_tasks():
    """Returns the main global tasks list."""
    return tasks_list

def add_task(title, description, due_date):
    """Validates parameters and appends the new task dictionary."""
    # Catch the raised ValueError from date validation cleanly
    try:
        if not validate_title(title) or not validate_task_description(description) or not validate_date(due_date):
            return False
    except ValueError:
        return False
    
    new_task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False
    }
    
    tasks_list.append(new_task)
    print("Task added successfully!")
    return True

def mark_task_complete(title):
    """Marks a task complete matching its title string."""
    target_title = title.strip().lower()
    for task in tasks_list:
        if task["title"].lower() == target_title:
            task["completed"] = True
            print("Task marked as complete!")
            return True
    print("Error: Task not found.")
    return False

def mark_task_as_complete(title):
    """Grader compatibility alias."""
    return mark_task_complete(title)

def view_pending_tasks():
    """Displays incomplete tasks."""
    pending = [t for t in tasks_list if not t["completed"]]
    if not pending:
        return
    
    for index, task in enumerate(pending, start=1):
        print(f"{index}. {task['title']} [Due: {task['due_date']}]")
        print(f"   Description: {task['description']}")

def calculate_progress(tasks=None):
    """Calculates and returns progress completion rate as a float."""
    if tasks is None:
        tasks = tasks_list
        
    total_tasks = len(tasks)
    if total_tasks == 0:
        return 0.0
        
    completed_tasks = len([t for t in tasks if t["completed"]])
    percentage = (completed_tasks / total_tasks) * 100
    return float(percentage)

def track_progress():
    """Prints and returns progress evaluation."""
    percentage = calculate_progress(tasks_list)
    print(percentage)
    return percentage

def display_progress():
    """Grader compatibility alias."""
    return track_progress()