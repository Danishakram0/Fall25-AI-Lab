tasks = []

def add():
    task = input("Enter a task: ")
    prty = input("Enter priority (High/Medium/Low): ")
    tasks.append({"task": task, "priority": prty})
    print(f"'{task}' added with {prty} priority")
def list():
    if len(tasks) == 0:
        print("No tasks")
    else:
        print("Current Tasks:")
        num = 1
        for i in tasks:
            print(f"{num}.{i['task']} (Priority:{i['priority']})")
            num += 1
def delete():
    list()
    try:
        delete = int(input("Enter the no to delete:"))
        if 1 <= delete <= len(tasks):
            removed = tasks.pop(delete - 1)
            print(f"Task no {delete} ({removed['task']}) deleted")
        else:
            print(f"Task no {delete} not found")
    except ValueError:
        print("Invalid input")

while True:
    print("Select one of the following option")
    print("1. Add task")
    print("2. Delete task")
    print("3. List tasks")
    print("4. Quit")
        
    choice = input("Enter your choice: ")
    if choice == "1":
        add()
    elif choice == "2":
        delete()
    elif choice == "3":
        list()
    elif choice == "4":
        break
    else:
        print("Invalid input")