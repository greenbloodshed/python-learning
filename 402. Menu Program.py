#==============#
# TASK MANAGER #
#==============#
#============================================================================================================================================================================================================================#
# This is a simple Menu Program that allows you to add, view, and remove tasks in a list. This program exemplifies truthy checks, try/except error handling, while and for loops, conditions, and python built in functions. #
#============================================================================================================================================================================================================================#
#==============#
# version: 1.0 #
#==============#


tasks = [] # start w/ an empty list

while True:                     # repeats forever… until we break.
    print("\nMenu:")            # \n is a 'newline char.' It tells Py to move to the next line before printing the rest.
    print("1. Add task")        # menu prints each loop.
    print("2. View tasks")
    print("3. Exit")
    print("4. Remove task")

    choice = input("Choose an option: ")    # prompts user to select an option from the list above.

    # Option 1(Add task)
    if choice == "1":
        task = input("Enter a task: ")      # prompts user to input a new task
        tasks.append(task)                  # ← adds the new task to the end of tasks list
        print("Task added succesfully")

    # Option 2(View tasks)
    elif choice == "2":
        if tasks:       # truthy check: empty list is False, non-empty is True
            print("Your tasks:")
            for index, task in enumerate(tasks, start=1):       # gets index per item in tasks list, starting at 1(instead of 0), and gets each item(task) in tasks list
                print(f"{index}. {task}")                       # prints what it gets ^
        else:
            print("No tasks yet.")

    # Option 3(Exit)
    elif choice == "3":
        print("Goodbye!")
        break

    # Option 4(Remove task)
    elif choice == "4":
        if tasks:       # truthy check
            print("Your tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                number = int(input("Enter the number of the task to remove: "))     # get a number from user input
                if 1 <= number <= len(tasks):           # len() returns the length of the collection(tasks)(how many items are in tasks)
                    removed = tasks.pop(number - 1)     # remove by index, converting to python index(starting at 0)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
            else:
                print("No tasks to remove.")

    else:
            print("Invalid option. Please try 1, 2, 3, or 4.")
