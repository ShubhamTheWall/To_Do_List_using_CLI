tasks = []

while True:

    print("\n----- TO DO LIST -----")
    print("1. Add Task What you Have To Do ")
    print("2. Show Tasks What are ")
    print("3. Delete Task")
    print("4. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:

        task = input("Enter task : ")
        tasks.append(task)
        print("Task Added")

    elif choice == 2:

        if len(tasks) == 0:
            print("No tasks available")
        else:
            print("\nYour Tasks : ")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif (choice==3):

        if len(tasks) == 0:
            print("No tasks available")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            number = int(input("Enter task number to delete : "))

            if number > 0 and number <= len(tasks):
                tasks.pop(number - 1)
                print("Task Deleted")
            else:
                print("Invalid task number")

    elif choice == 4:
        print("Program Ended")
        break

    else:
       print("Invalid Choice")