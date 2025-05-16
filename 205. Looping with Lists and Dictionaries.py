#========================================================================================================================
# Looping through lists and dictionaries
#========================================================================================================================

# Looping through lists
# Define a list of sports
sports = ["soccer", "football", "basketball"]

# Loop through the list
for sport in sports: # 'sport' can be anything. You're assigning this name, to each item in the list.
    print(f"I like {sport}.") # Output: I like soccer I like football I like basketball

# Looping through a dictionary

person = {
    "name": "Alice",
    "age": 30,
    "city": "NY"
}

# Keys Only: Default behavior when looping directly over the dictionary.
for key in person:
    print(key) # Output: name age city

# Values Only: Use the '.values()' method(This prints every value in the person dictionary)
for value in person.values():
    print(value) # Output: Alice 30 NY

# Both Keys and Values: Use the '.items()' method(This prints every key-value pair in the person dictionary)
for key, value in person.items():
    print(f"{key}: {value}") # Output: name: Alice age: 30 city: NY
