#==========================================================================================
# Lists
#==========================================================================================

# Creating a list
fruits = ["apple", "banana", "cherry"]

# Python uses zero-based indexing. Above, apple is 0, banana is 1, cherry is 2
# Accessing list items
print(fruits[0]) # Output: apple

# Adding an item to the end of the list
fruits.append("orange")

# Removing an item from the list
fruits.remove("banana")

# Iteration
for fruit in fruits:
    print(fruit)

    # OR
    for fruit in fruits:
        print(f"I like {fruit).")
