import time
from pathlib import Path

FILEPATH = Path('TO_do_simple.txt')
NEW_FIlEPATH = Path('Previous_todo.txt')

def get_current_date():
    return time.strftime('%b/%d/%y')

def read_tasks():
    if FILEPATH.exists():
        with open(FILEPATH, 'r') as file:
            return [task.strip() for task in file.readlines() if task.strip()]
    return []

def write_tasks(tasks):
    with open(FILEPATH, 'w') as file:
        file.write('\n'.join(tasks))

def add_task(task):
    tasks = read_tasks()
    tasks.append(task.strip())
    write_tasks(tasks)
    return f"'{task}' has been added to the list"

def show_tasks():
    return read_tasks()


def write_completed_tasks(tasks):  # Ensure 'tasks' is a list
    with open(NEW_FIlEPATH, 'w') as file:
        file.write('\n'.join(tasks) + '\n')  # Write each task on a new line

def read_completed_tasks():
    if NEW_FIlEPATH.exists():  # Added check for file existence
        with open(NEW_FIlEPATH, 'r') as file:
            return [task.strip() for task in file.readlines() if task.strip()]
    return []   

def edit_task(old_task, new_task):
    tasks = read_tasks()
    try:
        index = tasks.index(old_task.strip())
        tasks[index] = new_task.strip()
        write_tasks(tasks)
        return f"Task '{old_task}' has been updated to '{new_task}'"
    except ValueError:
        return "Task not found."

def delete_task(task):
    tasks = read_tasks()
    try:
        write_completed_tasks([task])  # Pass the task as a list
        tasks.remove(task)
        write_tasks(tasks)
        return f"Deleted task: {task}"
    except ValueError:
        return "Task not found."
