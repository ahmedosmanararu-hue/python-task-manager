"""
Validation module for task management system.
Contains functions to validate user input for task details.
"""

from datetime import datetime
from typing import Tuple

def validate_task_title(title: str) -> None:
    """
    Validate the task title.
    
    Args:
        title (str): The task title to validate
        
    Raises:
        ValueError: If the title is invalid
    """
    if not title or not isinstance(title, str):
        raise ValueError("Task title cannot be empty.")
    
    title = title.strip()
    if len(title) == 0:
        raise ValueError("Task title cannot be empty or just whitespace.")
    
    if len(title) > 100:
        raise ValueError("Task title must be 100 characters or less.")

def validate_task_description(description: str) -> None:
    """
    Validate the task description.
    
    Args:
        description (str): The task description to validate
        
    Raises:
        ValueError: If the description is invalid
    """
    if description is None:
        return  # Description is optional
    
    if not isinstance(description, str):
        raise ValueError("Description must be text.")
    
    description = description.strip()
    
    if len(description) > 500:
        raise ValueError("Task description must be 500 characters or less.")

def validate_due_date(due_date: str) -> None:
    """
    Validate the due date format.
    
    Args:
        due_date (str): The due date to validate in YYYY-MM-DD format
        
    Raises:
        ValueError: If the due date is invalid
    """
    if not due_date or not isinstance(due_date, str):
        raise ValueError("Due date cannot be empty.")
    
    due_date = due_date.strip()
    
    # Check format
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD format (e.g., 2024-12-31).")

def validate_task_data(title: str, description: str, due_date: str) -> None:
    """
    Validate all task data at once.
    
    Args:
        title (str): Task title
        description (str): Task description
        due_date (str): Task due date
        
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