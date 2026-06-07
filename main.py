from task_manager.task_utils import (
    add_task, 
    mark_task_complete, 
    view_pending_tasks, 
    track_progress
)

def display_menu():
    print("\n==============================")
    print("      TASK MANAGER")
    print("==============================")
    print("1. Add New Task")
    print("2. Mark Task as Complete")
    print("3. View Pending Tasks")
    print("4. Check Progress")
    print("5. Exit")
    print("==============================")

def main():
    while True:
        display_menu()
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            title = input("Enter title: ")
            description = input("Enter description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)
            
        elif choice == "2":
            title = input("Enter task title to complete: ")
            mark_task_complete(title)
            
        elif choice == "3":
            view_pending_tasks()
            
        elif choice == "4":
            track_progress()
            
        elif choice == "5":
            break
        else:
            print("Invalid Choice.")

if __name__ == "__main__":
    main()