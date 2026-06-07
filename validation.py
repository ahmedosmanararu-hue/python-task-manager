from datetime import datetime
from typing import Tuple


def validate_task_title(title: str) -> bool:
    """
    Validate the task title.
    
    Args:
        title: Task title to validate
        
    Returns:
        bool: True if valid
        
    Raises:
        ValueError: If title is invalid
    """
    if not isinstance(title, str):
        raise ValueError("Task title must be a string.")

    trimmed = title.strip()
    if len(trimmed) == 0:
        raise ValueError("Task title cannot be empty.")

    if len(trimmed) > 100:
        raise ValueError("Task title must be 100 characters or less.")

    return True


def validate_task_description(description: str) -> bool:
    """
    Validate the task description.
    
    Args:
        description: Task description to validate
        
    Returns:
        bool: True if valid
        
    Raises:
        ValueError: If description is invalid
    """
    if description is None:
        return True

    if not isinstance(description, str):
        raise ValueError("Task description must be text.")

    trimmed = description.strip()
    if len(trimmed) > 500:
        raise ValueError("Task description must be 500 characters or less.")

    return True


def validate_due_date(due_date: str) -> bool:
    """
    Validate the due date format.
    
    Args:
        due_date: Due date in YYYY-MM-DD format
        
    Returns:
        bool: True if valid
        
    Raises:
        ValueError: If due date is invalid
    """
    if not isinstance(due_date, str):
        raise ValueError("Due date must be text in YYYY-MM-DD format.")

    trimmed = due_date.strip()
    if len(trimmed) == 0:
        raise ValueError("Due date cannot be empty.")

    try:
        datetime.strptime(trimmed, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD format.")

    return True


def validate_task_data(title: str, description: str, due_date: str) -> bool:
    """
    Validate all task data at once.
    
    Args:
        title: Task title
        description: Task description
        due_date: Due date
        
    Returns:
        bool: True if all valid
        
    Raises:
        ValueError: If any validation fails, with combined error messages
    """
    errors = []
    
    try:
        validate_task_title(title)
    except ValueError as e:
        errors.append(str(e))
    
    try:
        validate_task_description(description)
    except ValueError as e:
        errors.append(str(e))
    
    try:
        validate_due_date(due_date)
    except ValueError as e:
        errors.append(str(e))
    
    if errors:
        raise ValueError("; ".join(errors))
    
    return True