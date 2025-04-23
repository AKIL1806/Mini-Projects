def show_menu():
    print("\n---To-Do-List---")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Clear All Tasks")
    print("4.Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        with open("todo.txt","a") as file:
            file.write(task + "\n")
        print("Task added!")

    elif choice == "2":
        with open("todo.txt","r") as file:
            print(file.read())

    elif choice == "3":
        with open("todo.txt","w") as file:
            pass
        print("All Tasks Cleared!")

    elif choice == "4":
        print("GoodBye!")
        break

    else:
        print("Invalid choice. Please try again")

    