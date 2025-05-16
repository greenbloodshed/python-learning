#==================================================================================================================================================================================================================================================
# Here are some notes I took on Syntax in the beginning.
# OH! Another good reference, which I use, was made by one of my favorite podcasters, Jack Rhysider, of DarkNet Diaries. You can find his cheat sheet here: https://www.tunnelsup.com/python-cheat-sheet/ , and I highly recommend Jack's podcast.
#==================================================================================================================================================================================================================================================

#----------------------------------------------------------------------------------------------------------------------------------
# Comments are used to explain code - starting a line w/ '#' indicates a comment.

''' Comments do not execute. You can use triple quotes for multi line comments
    like this one '''


#----------------------------------------------------------------------------------------------------------------------------------
# Python uses indentation to define blocks of code. Indent = 4 spaces.

# Example
if True:
    print("This is ture.")


#----------------------------------------------------------------------------------------------------------------------------------
# Variables:
# Variables are created when you assign value to them. Python is dynamically typed. This means you don't need to assign value to them.

# Example
x = 5
y = "Hello, World!"


#----------------------------------------------------------------------------------------------------------------------------------
# Data Types
# Integers (int), floating-point numbers (float), strings (str), and booleans (bool)

# Example
int = 1
float = 1.5
strings = "This is a string"
bool = True


#----------------------------------------------------------------------------------------------------------------------------------
# Functions
# functions are defined using the 'def' keyword, short for definition. They can take arguments and return values.

# Example (see '202. Functions' for more examples and deeper explanation)
def my_function():
    print("Hello World!")

# There are many built in functions in python. See: https://docs.python.org/3/library/functions.html


#----------------------------------------------------------------------------------------------------------------------------------
# Loops and conditional statements(see 2nd, 9th, and 10th programs for examples and explanation)
# A 'for loop' is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence.)

# For loops
# Example
for item in sequence:
    # 'Block of code to execute here'

# Example of list iteration
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# While loops
# Example
    
while condition:
    # 'Block of code to executer here'

count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1 # This is crucial to ensure the loop evantually ends

# Using break in loops
    
for number in range(1, 10):
    if number == 5:
        break # Exit the loop
    print(number)

# Using continue
    for number in range(1, 10):
        if number == 5:
            continue # Skip to the next iteration
        print(number)


#----------------------------------------------------------------------------------------------------------------------------------
# Arithmetic Operators
''' Operator            |      Name            |           Example '''

    +                          Addition                    x + y
    -                          Subtraction             	   x - y
    *                          Multiplication              x * y
    /                          Division                    x / y
    %                          Modulus                     x % y
    **                         Exponentiation              x ** y
    //                         Floor division              x // y
#----------------------------------------------------------------------------------------------------------------------------------

''' In computing and mathematics, the modulo operation returns the remainder or signed remainder of a division, after one number is divided by another, the latter being called the modulus of the operation.
    E.g., "5 % 2" evaluates to 1, because 5 divided by 2 has a quotient of 2 and a remainder of 1. '''

