# Functions
# A function in Python is defined using the def keyword, followed by a name, parentheses (), and a colon :. The indented block of code following the colon is the body of the function, where you define what the function does.

# Defining a function: 'def'
def greet():
    print("Hello World!")

# Calling the function
greet()


# ----------------------------------------------------------------------
# Functions w/ Parameters
# Functions can take parameters (also known as arguments), which are values you pass into the function to modify its behavior or output.

# Function w/ a parameter
name = input("What is your name?")

def greet(name):
    print(f"Hello, {name}!")

# Calling the function w/ a parameter
greet(f"{name}")


# ----------------------------------------------------------------------
# Functions can also return values using the return statement. This is useful when you want the function to calculate a result and make it available to the rest of your program.

# Function that returns a value
def add(a, b):
    return a + b

# Calling the function and storing its result
result = add(3, 4)
print(result)  # Output: 7


#----------------------------------------------------------------------
# Calculate the Area of a triangle
# Area = .5 * base * height

#Function to calculate area of a triangle
def calculate_area(base, height):
    area = 0.5 * base * height
    return area

area = calculate_area(10, 5)
print(f"The area of the triable is: {area}")

# Understanding the Function
# Function Definition: The def keyword starts the definition of the function, followed by the function name (calculate_area) and the parameters it takes (base and height) enclosed in parentheses.

# Calculating the Area: Inside the function, the area is calculated using the formula 0.5 * base * height and stored in a local variable named area.

# Returning the Result: The return statement is used to return the calculated area back to the caller.

# Calling the Function: To use this function, you call it with the base and height as arguments, store the result it returns in a variable (area in this case), and then print or use the result as needed. '''
