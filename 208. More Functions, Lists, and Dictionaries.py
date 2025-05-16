#==============================================================================================================
# More functions, lists, & dictionaries
#==============================================================================================================


#--------------------------------------------------------------------------------------------------------------
# Defining a Function to Process a List:
def print_list_elements(my_list):
    for item in my_list:
        print(item)

# 'def print_list_elements(my_list):':
    # def' is the keyword to define a function.
    # print_list_elements' is the function name.
    # 'my_list' is a parameter. When the function is called 'my_list' will refer to the list passed to the function. 
    # 'my_list' in this instance, serves as a placeholder for a future list.

        # 'for item in my_list:':
            # 'for' is a keyword to start a for-loop.
            # 'item' is a variable that takes on each value in 'my_list' as the loop iterates through the list.
            # 'my_list' is the parameter received by the function, expected to be a list.

                # 'print(item)':
                    # Inside the loop, each 'item' is printed. 


# Calling a Function w/ a List:
fruits = ["apple", "banana", "cherry"] # This is a list.
print_list_elements(fruits) # Here, we call the function we created, and pass the list we created as the arguement.


#--------------------------------------------------------------------------------------------------------------
# Defining a Function to Process a Dictionary:
def print_computer_specs(computer_specs):
    for key, value in computer_specs.items():
        print(f"{key}: {value}")

# 'def print_computer_specs(computer_specs):':
    # 'def' keyword defines the function.
    # 'print_computer_specs' is the function name.
    # 'computer_specs' is a parameter. When the function is called, 'computer_specs' will refer to the arguement passed to the function. In this instance, 'computer_specs' is a placeholder for any dictionary.

        # 'for key, value in computer_specs.items():':
            # 'for' starts a for-loop.
            # 'key' and 'value' are variables that take on the key-value pairs of the dictionary.
            # 'computer_specs.items()' returns a view object that displays a list of a dictionary's key-value tuple pairs.

                # 'print(f"{key}: {value}")':
                    # Inside the loop, each key-value pair is printed in the format 'key: value'.


# Calling a Function w/ a Dictionary:
computer = {            # Lines 53 - 57 make up a dictionary.
    "brand": "Dell",
    "model": "XPS 15",
    "year": 2020
}

print_computer_specs(computer) # Here, we call the function, passing the 'computer' dictionary as the argument.


#--------------------------------------------------------------------------------------------------------------
# Key Points:

# Parameters and Arguments:
    # When defining a function, parameters like 'my_list' and 'computer_specs' are placeholders.
    # When Calling a function, arguments like 'fruits' and 'computer' are the actual data passed to these placeholders.
    
# Dynamically Typed Language:
    # In Python, you don't have to specify the type of the paramter ('list' or 'dictionary') explicitly.
    # The function works w/ any list OR dictionary passed to it, as long as you use appropriate methods ('for item in my_list' for lists, or '.items()' for dictionaries).

# Reusability:
    # Functions designed this way are reusable. You can pass any list to 'print_list_elements' or any dictionary to 'print_computer_specs', and the function will process it appropriately.

