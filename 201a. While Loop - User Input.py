# While loop w/ user input

while True:                                                               # This line(3) starts an infinite loop. True is a Boolean value that always evaluates to true, so the loop will continue to run indefinitely unless explicitly broken out of with a break statement.
    user_input = input("Type something (or ''exit' to stop): ")           # This line prompts the user to type something into the console. Whatever the user types is then stored as a string in the variable user_input.
    if user_input.lower() == "exit":                                      # .lower() converts the string stored in 'user_input' to lowercase
        break
    else:
        print(f"You typed: {user_input}")



# Line 5 checks if the user wants to exit the loop. The .lower() method converts the string stored in user_input to lowercase. This ensures that the comparison is case-insensitive, meaning it doesn't matter if the user types "exit", "Exit", "EXIT", etc.; all will be considered a match.
# If the condition user_input.lower() == "exit" is true (i.e., the user typed "exit" regardless of capitalization), the break statement is executed. break immediately exits the closest enclosing loop, in this case, the while True loop.
# If the condition is not true (the user types anything other than "exit"), the else block executes, printing the message You typed: {user_input}. The {user_input} part is replaced by whatever the user typed, demonstrating how to incorporate user input into a string that's being printed.
