"""
Validation module for task management system.
Contains functions to validate user input for task details.
"""

from datetime import datetime

def validate_task_title(title):
    """
    Validate the task title.
    
    Args:
        title (str): The task title to validate
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not title or not isinstance(title, str):
        return False, "Task title cannot be empty."
    
    title = title.strip()
    if len(title) == 0:
        return False, "Task title cannot be empty or just whitespace."
    
    if len(title) > 100:
        return False, "Task title must be 100 characters or less."
    
    return True, None

def validate_task_description(description):
    """
    Validate the task description.
    
    Args:
        description (str): The task description to validate
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if description is None:
        return True, None  # Description is optional
    
    if not isinstance(description, str):
        return False, "Description must be text."
    
    description = description.strip()
    
    if len(description) > 500:
        return False, "Task description must be 500 characters or less."
    
    return True, None

def validate_due_date(due_date):
    """
    Validate the due date format and ensure it's not in the past.
    
    Args:
        due_date (str): The due date to validate in YYYY-MM-DD format
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not due_date or not isinstance(due_date, str):
        return False, "Due date cannot be empty."
    
    due_date = due_date.strip()
    
    # Check format
    try:
        parsed_date = datetime.strptime(due_date, "%Y-%m-%d")
        
        # Check if date is not in the past (allow today)
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        if parsed_date < today:
            return False, "Due date cannot be in the past."
        
        return True, None
        
    except ValueError:
        return False, "Invalid date format. Please use YYYY-MM-DD format (e.g., 2024-12-31)."

def validate_task_data(title, description, due_date):
    """
    Validate all task data at once.
    
    Args:
        title (str): Task title
        description (str): Task description
        due_date (str): Task due date
        
    Returns:
        tuple: (is_valid, list_of_errors)
    """
    errors = []
    
    # Validate title
    title_valid, title_error = validate_task_title(title)
    if not title_valid:
        errors.append(title_error)
    
    # Validate description
    desc_valid, desc_error = validate_task_description(description)
    if not desc_valid:
        errors.append(desc_error)
    
    # Validate due date
    date_valid, date_error = validate_due_date(due_date)
    if not date_valid:
        errors.append(date_error)
    
    return len(errors) == 0, errors