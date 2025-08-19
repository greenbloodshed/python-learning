#===================================================================================
# Conditions/Control Flow Exercises w/ User Input
#===================================================================================

# Exercise 1: Sign Test
# Asks the user for an integer and prints "Positive", "Zero", or "Negative".

n = int(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n == 0:
    print("Zero")
else:
    print("Negative")


# Exercise 2: Ticket Price by age
# Asks the user for an integer(Age), and outputs ticket cost by age

age = int(input("Ticket costs are different depending on age. How old are you?: "))
if age < 3:
    print("$0")
elif age <= 12:
    print("$10")
elif age < 65:
    print("$20")
else:
    print("$12")

# Exercise 3: Command loop w/ exit

while True:
    cmd = input("Type a command (or 'exit'): ").strip().lower()
    if cmd == "exit":
        print("Bye!")
        break
    elif cmd == "help":
        print("Available: help, exit")
    else:
        print(f"Unknown command: {cmd}")
