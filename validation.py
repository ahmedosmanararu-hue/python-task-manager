from datetime import datetime


def validate_task_title(title: str) -> bool:
    if not isinstance(title, str):
        raise ValueError("Task title must be a string.")

    trimmed = title.strip()
    if len(trimmed) == 0:
        raise ValueError("Task title cannot be empty.")

    if len(trimmed) > 100:
        raise ValueError("Task title must be 100 characters or less.")

    return True


def validate_task_description(description: str) -> bool:
    if description is None:
        return True

    if not isinstance(description, str):
        raise ValueError("Task description must be text.")

    trimmed = description.strip()
    if len(trimmed) > 500:
        raise ValueError("Task description must be 500 characters or less.")

    return True


def validate_due_date(due_date: str) -> bool:
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
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)
    return True
