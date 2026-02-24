todo_list = []

#Function to display a menu
def add_task():
    task = input("Enter a task:")
    todo_list.append({"Task": task, "status": "pending"})
    print("New task added successfully!\n")


#Function to view All Tasks
def view_task():
    print("Your Todo List:")
    if len(todo_list) ==0:
        print("No pending tasks!")
    else:
        for index, task in enumerate(todo_list, 1): #enumerate is an inbuilet function that adds a counter to an iterable. -> enumerate(iterable , start_index)
            print(f"{index}: {task["Task"]} - {task['status']}")
    print("\n")

#Function to Remove task
def remove_task():
    if len(todo_list)==0:
        print("List is Empty!")
    else:
        search_index = int(input("Enter the task number that you want to remove: "))
        if 0 <= search_index < len(todo_list):
            removed_task = todo_list.pop(search_index)
            print(f"Task Removed:{removed_task}")
        else:
            print("Invalid Task Number")


def menu():
    while(True):
        print("*** Main Menu")
        print(" 1. Add a new task")
        print(" 2. view all task")
        print(" 3. Remove a task")
        print(" 4. Mark a task as compled")
        print(" 5. Exit")

        choice = input("Enter your choice:")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice =="4":
            mark_done()
        elif choice == "5":
            print("Exitiing the application...")
            exit()
        else:
            print("Invalid choice! Try again!!")

menu()