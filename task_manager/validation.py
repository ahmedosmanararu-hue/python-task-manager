import datetime

def validate_title(title):
    """Validates the task title matches the required name in __init__.py."""
    if not title or not isinstance(title, str) or not title.strip():
        print("Validation Error: Title cannot be empty.")
        return False
    if len(title) > 50:
        print("Validation Error: Title must be 50 characters or less.")
        return False
    return True

def validate_task_description(description):
    """Validates the description."""
    if not description or not isinstance(description, str) or not description.strip():
        print("Validation Error: Description cannot be empty.")
        return False
    if len(description) > 200:
        print("Validation Error: Description must be 200 characters or less.")
        return False
    return True

def validate_date(date_string):
    """Validates the due date format matches the required name in __init__.py."""
    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        print("Validation Error: Invalid date format. Please use YYYY-MM-DD.")
        return False