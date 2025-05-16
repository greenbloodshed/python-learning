#==============================================================================================================
# Dictionaries
#==============================================================================================================

# A dictionary is an unordered collection of items. Each item in a dictionary has a key/value pair. Dictionaries are mutable, allowing you to add, remove, or modify items.

# Crating a dictionary
person = {
    "name": "Bill",
    "age": 50,
    "city": "ATL"
}

# Accessing dictionary values
print(person["name"]) # Output: Bill

print(person["age"]) # Output: 50

# Adding or updating a key/value pair
person["email"] = "test@example.com"

# Removing an item
del person["age"]

# Iterating over a dictionary (keys)
for key in person:
    print(key, person[key])

# Iterating over key/value pairs
for key, value in person.items():
    print(key, value)
