todo_list = []

#Function to display a menu
def add_task():
    task = input("Enter a task:")
    todo_list.append({"Task": task, "status": "pending"})
    print("New task added successfully!")
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