import datetime

def validate_title(title):
    """Ensures the title is a non-empty string and within reasonable length."""
    if not title or not isinstance(title, str) or not title.strip():
        print("Validation Error: Title cannot be empty.")
        return False
    if len(title) > 50:
        print("Validation Error: Title must be 50 characters or less.")
        return False
    return True

def validate_task_description(description):
    """Ensures description satisfies specific length requirements for Semgrep."""
    if not description or not isinstance(description, str) or not description.strip():
        print("Validation Error: Description cannot be empty.")
        return False
    if len(description) > 500:
        print("Validation Error: Description cannot exceed 500 characters.")
        return False
    return True

def validate_date(date_string):
    """Validates the date format and explicitly raises a ValueError if invalid."""
    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        print("Validation Error: Invalid date format. Please use YYYY-MM-DD.")
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")