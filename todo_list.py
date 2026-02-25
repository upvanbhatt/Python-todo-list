todo_list = []

#Function to Add a menu
def add_task():
    task = input("Enter a task:")
    todo_list.append({"Task": task, "status": "pending"})
    print("New task added successfully!\n")



#Function to view All Tasks
def view_task():
    print("Your to do List:")
    if len(todo_list) == 0:
        print("No pending task!")
    else:
        for index, task in enumerate(todo_list, 1): # enumerate is an inbuilt function that adds a counter to an iterable :-> enumerate(iterable , start_index)
            print(f"{index}: {task['Task']} - {task['status']}")
    print("\n")

#Function to remove a task
def remove_task():
    if len(todo_list)==0:
        print("\n List is empty!")
    else:
        try:
            search_index =int(input("Enter the task number that you want to remove:")) - 1
            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task Removed:{removed_task['Task']}")
            else:
                print("Invalid Task Number.")
        except ValueError:
            print("Please enter a Valid Task number.")

#Function to Mark a Task as Done
def mark_done():
    if len(todo_list)==0:
        print("\n List is empty!")
    else:
        try:
            search_index =int(input("Enter the task number that you want to mark as complete:")) - 1
            if 0 <= search_index < len(todo_list):
                todo_list[search_index]['Status'] = 'done'
                print(f"Task {todo_list[search_index]['Task']} has been marked as Dome.")
            else:
                print("Invalid Task Number.")
        except ValueError:
            print("Please enter a Valid Task number.")



#Function to display a Menu
def menu():
    while(True):
        print("*** Main Menu")
        print(" 1. Add a new task")
        print(" 2. view all task")
        print(" 3. Remove a task")
        print(" 4. Mark a task as completed")
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