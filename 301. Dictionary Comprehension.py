#==============================================================================================================
# Dictionary Comprehension
#==============================================================================================================

# List and Dictionary Comprehensions provide a concise way to create lists and dictionaries.
# Dictionary Comprehension is similar to list comprehension, but is used for creating dictionaries.


#--------------------------------------------------------------------------------------------------------------
# Syntax: 'new_dict = {key_expression: value_expression for item in iterable if condition}'
                      {key_expression: value_expression for item in iterable if condition}
    # 'key_expression': Expression for the key.
    # 'value_expression': Expression for the value.
    # 'item': The current item in the iteration.
    # 'iterable': The collection you are iterating over.
    # 'condition' (optional): A filter that selects which items to include.


# Creating a dictionary of squares
# This creates a dictionary where the keys are numbers from 0 to 9 and the values are their squares.
squares_dict = {x: x**2 for x in range(10)}

print(squares_dict)


# Filtering a dictionary
# This creates a dictionary containing only the items from original_dict where the value is even.
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_dict = {k: v for k, v in original_dict.items() if v % 2 == 0}

print(filtered_dict)
