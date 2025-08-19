todo_list = []

def add_task():
    task = input("enter a new task: ")
    todo_list.append(task)
    print(f"task {task} added to the todo list.")

def view_task():
    if not todo_list:
        print("the list is empty")
    else:
      for i in todo_list:
          print(i,end = " ")
        

def remove_task():
    task = input("enter the task to remove: ").strip()
    if task in todo_list:
        todo_list.remove(task)
        print(f"task {task} is removed from the todo list.")
    else:
        print("The item is not in the list")

while True:
    print("--------welcome----------")
    print("1: add task")
    print("2: view task")
    print("3: remove task")
    print("4: quit app")

    choice = input("enter choice: ")
    if choice == "1":
       add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        break
    else:
        print("enter valid input")
    


            