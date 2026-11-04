


import json


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: tasks.json contains invalid data.")
        raise SystemExit("Please fix the JSON file.")

tasks = load_tasks()

def add_task():
    title = input("Enter Task: ").strip()

    if not title:
        print('Invalid input')
        return

    priority = input("Enter priority level (low, medium, high): ").lower()
    if priority not in ["low", "medium" , "high"]:
        print('Invalid priority level')
        return

    tasks.append({
        "title" : title,
        "priority" : priority,
        "completed" : False
    })
    save_tasks()

    print('Task added successfully')

def view_tasks():
    if not tasks:
        print('Task list is empty')
        return

    for index, task in enumerate(tasks, start = 1):
        if not task["completed"]:
            status = "Pending"

        else:
            status = "Completed"

        print(f"\n{index}. Task: {task['title']} - Priority: {task['priority']} - Status: {status}")


def task_complete():
    try:
        view_tasks()
        number = input('which task are you done with? enter number').strip()
        int_number = int(number)
        if not int_number:
            print('Invalid input')
            return
        if 1 <= int_number <= len(tasks):
            tasks[int_number -1]['completed'] = True
            save_tasks()
            print('Task status has been updated')
    except ValueError:
        print('Invalid input')

    

def remove_task():
    view_tasks()
    number = input('which task are you done with? enter number').strip()
    int_number = int(number)
    if not int_number:
        print('Invalid input')
        return
    tasks.pop(int_number - 1)
    save_tasks()
    print('Task has been removed')


def high_priority_task():
    
    for index, task in enumerate(tasks, start=1):
        if task.get('priority') == 'high':
            print(f"{index}. {task['title']}  ")

def pending_task():
    for index, task in enumerate(tasks, start=1):
        if task.get('completed') == False:
            print(f"{index}. {task['title']}  ")
while True:
    
    
        print('\n1. View Task \n 2. Add task \n 3. remove task \n 4.Update task \n 5. high priority tasks \n 6. pending task \n 0. quit')
        number = input('Enter number: ').strip()
        if not number:
            print('Invalid input')

        elif number == '1':
            view_tasks()

        elif number == '2':
            add_task()

        elif number == '3':
            remove_task()

        elif number == '4':
            task_complete()

        elif number == '5':
            high_priority_task()

        elif number == '6':
                pending_task()

        elif number == '0':
            print('Bye')
            break

   

        
    