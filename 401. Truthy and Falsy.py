#=======================================================================================================
# Truthy and Falsy
#=======================================================================================================

# When you write an if statement, Python expects a condition — something that is either True or False.

# But Python doesn’t require the condition to literally be True or False. 
# Many other values can be interpreted as True or False.

# Values that Python treats as False → we call them falsy
# Everything else → truthy


#==============================
# Falsy values (memorize these)
#==============================

#Python considers the following as False:

False    # (the Boolean false itself)
None     # (special “nothing” value in Python)
0        # (the integer zero)
0.0      # (zero as a float)
""       # (empty string)
[]       # (empty list)
{}       # (empty dictionary)
set()    # (empty set)
()       # (empty tuple)

# That’s basically it!


#==============
# Truthy Values
#==============

# Everything that is not falsy is truthy
# Examples:

42, -1, 3.14    # Any non-zero number

"hello", " "    # Any non-empty string

[1, 2, 3]       # Any non-empty list/dictionary/etc:
{"a": 1}        # truthy
(5,)            # truthy


#============================
# Why is this useful to know?
#============================

# It lets you write cleaner, shorter code.
# Example 1: Checking if a string is empty:

name = ""

if name:    # instead of if name != ""
    print("Has a name")
else:
    print("Empty")
# Prints 'Empty'

# Example 2: Checking if a list has items

fruits = ["apple", "banana"]

if fruits:
    print("We have fruits!")    # runs
else:
    print("No fruits")
# If fruits = [] (empty), it would print: 'No fruits'

# Example 3: Checking numbers

n = -5

if n:
    print("Non-zero")
else:
    print("Zero")
# Prints 'Non-zero' b/c any non-zero number is truthy.


#=============================
# Explicit vs. Implicit checks
#=============================

# Sometimes you want to be explicit for clarity:
if len(fruits) > 0:
    print("We have fruits")

# Other times you can use the implicit truthy/falsy shortcut:
if fruits:
    print("We have fruits")

# Both are correct — it’s a matter of style and clarity.


#====================
# Additional Examples
#====================

# Example 1
#--------------------

if 0:
    print("A")
else:
    print("B")
# 0 is falsy
# So the 'if' branch is skipped --> goes to else.
# Prints B


# Example 2
#--------------------

if " ":
    print("C")
else:
    print("D")
# " " is a string containing a space. It's not empty.
# Non-empty strings are truthy.
# Prints C


# Example 3
#--------------------

if []:
    print("E")
else:
    print("F")
# [] is an empty list, and empties are falsy
# So it skips if and runs else.
# Prints F
