#==============================================================================================================
# List Comprehension
#==============================================================================================================

# List and Dictionary Comprehensions provide a concise way to create lists and dictionaries.
# A list comprehension provides a compact way to process all or part of the elements in a collection and return a list.


#--------------------------------------------------------------------------------------------------------------
# Syntax: 'new_list = [expression for item in iterable if condition]'
                      [expression for item in iterable if condition]
    # 'expression': The expression to evaluate for each item.
    # 'item': The current item in the iteration.
    # 'iterable': The collection you are iterating over.
    # 'condition' (optional): A filter that selects which items to include.


# Creating a list of squares (This creates a list of squares of numbers from 0 to 9)
# with 'squares = [....]' you are creating a list. We use list comprehension here to say "make a list of numbers 0-9 to the power of 2."
squares = [x**2 for x in range(10)]

print(squares)


# Filtering a list (This creates a list of even numbers from 0 to 9)
# Here, we add a condition, saying "make a list of numbers from 0-9, if they are even numbers."
even_numbers = [x for x in range(10) if x % 2 == 0]

print(even_numbers)
