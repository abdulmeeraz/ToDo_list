
import os
import json

def load_task(filename = "tasks.json"):
    if os.path.exists(filename):
        with open(filename,"r") as file:
            return json.load(file)
    return[]

def save_task(tasks,filename = "tasks.json"):
    with open(filename,"w") as file:
        json.dump(tasks,file,indent=4)


def show_menu():
    print("\n====== TO-DO LIST ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


def add_task(tasks):
    task = input("Enter task description: ")
    tasks.append({"task": task, "completed": False})
    save_task(tasks)
    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        save_task(tasks)
        print(f"{i}. {task['task']} [{status}]")


def mark_task_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Enter task number to mark as completed: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_task(tasks)
            print(f"Task '{removed['task']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def todo_app():
    tasks = load_task()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye! Stay productive 😊")
            break
        else:
            print("Invalid choice! Please try again.")


todo_app()
