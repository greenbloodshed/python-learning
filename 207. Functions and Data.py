#========================================================================================================================
# Functions Involving Lists and Dictionaries
#========================================================================================================================

# Writing functions that accept lists or dictionaries as parameters can make your code more modular and reusable.


#------------------------------------------------------------------------------------------------------------------------
# Function w/ a list parameter
list = ["thing", "thing1", "thing2"]

def list_processor(list):
    for item in list:
        print(f"Processing {item}...")

  # Example usage
list_processor(list) # Output: Processing thing... Processing thing1... Processing thing2...


#------------------------------------------------------------------------------------------------------------------------
# Function w/ a dictionary parameter
person = {
    "name": "Alice",
    "age": 30,
    "city": "NY"
}

def print_person_info(person):
    for key, value in person.items():
        print(f"{key}: {value}")

print_person_info(person) # Output name: Alice age: 30 city: NY


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
''' When you define a function, you specify parameters that will receive the actual values (arguments) passed to the function when it is called. These parameters are placeholders that allow your function to operate on different lists or dictionaries (or other data types) each time the function is called. '''
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Function syntax:
''' def function_name(parameters):
        block of code'''

# 'def' tells Py that you're defining a function.
# 'function_name' is the name you're giving to the function. It should be descriptive and adhere to Py naming conventions.
# 'parameters' are the inputs to the function. You can define none, one, or several parameters seperated by commas. When working with lists and dictionaries, these parameters can be lists or dictionaries.
# The indented block of code beneath the 'def' line is the body of the function, where you you define what the function does.


# Example: Lists in Functions:
# You can pass a list as a parameter to a function to do things like add items, rm items, iterate over the list to process its items.

computers = ["PC1", "PC2", "PC3", "PC4"] # List of hostnames

def print_list_elements(my_list): # Creating a function
    for item in my_list: # Body of the function. This function lists all the hostnames in the computers list.
        print(item)


# Example: Dictionaires in functions:
# Passing dictionaries to functions allows you to access and manipulate key-value pairs. You can iterate over the dictionary, add or rm key-value pairs, or modify values.

computers_specs = {
    "PC1": "1.5 GHz CPU, 4GB RAM",
    "PC2": "2.5 GHz CPU, 8GB RAM",
    "PC3": "3.5 GHz CPU, 16GB RAM",
    "PC4": "6.95 GHz CPU, 128GB RAM"
}

def print_key_values(dict):
    for key, value in dict.items():
        print(f"{key}: {value}")

# Calling Functions w/ List and Dictionary Arguments
        
print_list_elements(computers)
print_key_values(computers_specs)

# The names of the parameters in the 2 funtions created above, 'my_list' and 'dict' can be anything. When you call a function, and insert a list or dictionary, and the body of the funtion uses the arguement correctly it will work.
# For example, in the first function, 'my_list' is just a placeholder. When you call 'print_list_elements(computers)' the 'computers' list is passed to 'print_list_elements', and inside the function 'my_list' will refer to 'computers'.
# ^ same applies to the other function built to print key and values from dictionaries. The placeholder refers to the dictionary.
