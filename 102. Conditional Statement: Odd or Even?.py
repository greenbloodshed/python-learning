#==============================================================================================================
# Conditional statement (if, then, else, elif)
#==============================================================================================================

''' This code checks whether or not a number is even. It gets a number from user input and stores it as the variable 'number', and converts the string to an integer.
    Then, the code checks if 'number' divided by 2 has a remainder of 0 using the modulo operator(%) and if so, it outputs: "This is an even number." Otherwise, it prints: "This is an odd number."'''

# Get the number from the user and convert it to an integer
number = int(input("Enter a number: "))

# Check if the number is even
if number % 2 == 0:
    print("This is an even number.")
# If the number is not even, it must be odd
else:
    print("This is an odd number.")
