import json
import os

# Define the filename for storing tasks
FILENAME = "tasks.json"

# Load tasks from the file if it exists
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to the file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(description):
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "description": description, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {description}")

# Remove a task by its ID
def remove_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    for index, task in enumerate(tasks):
        task["id"] = index + 1
    save_tasks(tasks)
    print(f"Task {task_id} removed.")

# List all tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for task in tasks:
            status = "✓" if task["completed"] else "✗"
            print(f"[{status}] {task['id']}: {task['description']}")

# Mark a task as completed
def mark_completed(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            break
    save_tasks(tasks)
    print(f"Task {task_id} marked as completed.")

# Display the command menu
def show_menu():
    print("\nTo-Do List Application")
    print("-----------------------")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. List tasks")
    print("4. Mark task as completed")
    print("5. Exit")

# Main application loop
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            description = input("Enter task description: ")
            add_task(description)
        elif choice == "2":
            try:
                task_id = int(input("Enter task ID to remove: "))
                remove_task(task_id)
            except ValueError:
                print("Invalid task ID. Please enter a number.")
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                mark_completed(task_id)
            except ValueError:
                print("Invalid task ID. Please enter a number.")
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
