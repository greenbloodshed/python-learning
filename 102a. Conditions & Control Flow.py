#=======================================================================================================
# Conditions (True or False)
#=======================================================================================================

# A condition is just an expression that Python can evaluate to True or False
# Comparison Operators

5 == 5    # True    (equal to)
5 != 3    # True    (not equal)
7 < 10    # True
7 <= 7    # True
9 > 2     # True
9 >= 10   # True


#=======================================
# Logical Operators (combine conditions)
#=======================================

(5 <10) and (2 == 2)    # True  only if both are True
(5 < 10) or (2 == 3)    # True  if at least one is True
not (5 < 10)            # False  flips True to False


#======================
# The basic 'if' syntax
#======================

if <condition>:
    # indented block runs only if condition is True

# Colon ':' end the 'if' line.
# Indentation (typically 4 spaces) defines the block.
# Python uses indentation to mark "what belongs to what."

# Example

age = 30

if age >= 18:
    print("Adult")    # runs b/c the condition is True


#=======================================================
# Adding 'else' (what to do when the condition is False)
#=======================================================

# Example

age = 10

if age >= 18:
    print("Adult")
else:
    print("Not an Adult")    # runs b/c the if condition is False


#==================================================================
# Adding 'elif' (check another condition if the previous was False)
#==================================================================

# Use 'elif' for manually exclusive branches:
# Example 1

age = 16

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
# Only one branch runs: the first whose condition is True

# Example 2
number = 0

if number > 0:            # Check 'number > 0' --> False
    print("Positive")
elif number == 0:         # Check 'number == 0' --> True --> prints/outputs 'Zero'
    print("Zero")
else:                     # 'else' is skipped b/c an earlier branch was matched.
    print("Negative")


#=====================
# Combining Conditions
#=====================

# Sometimes you need more than one condition:
# Example

age = 25
member = True

if (18 <= age < 65) and member:    # This is a chained comparison. It is cleaner than (age >= 18 and age < 65)
    print("Discount applies")          # 'and' requires both sides be True.
else:                                      # 'or' would accept either side being True.
    print("No discount")


#==================================
# Strings & case-insensitive checks
#==================================

# User input can be uppercase or lowercase. Normalize it:
# Example

cmd = "Exit"

if cmd.lower() == "exit":
    print("Goodbye!")
# .lower() turns "Exit" into "exit" so the comparison works regardless of how the user typed it.


#=====================================
# Truthy / Falsy (advanced-but-useful)
#=====================================

# Some values act like False in conditions:
    # Falsy: 0,"" (empty string), [] (empty list), {} (empty dict), None, False
    # Truthy: almost everything else

# Example

name = ""

if name:                       # ** Remember, an 'if' statement checks if a condition is True, that's it **
    print("We have a name.")
else:
    print("Name is empty.")    # runs b/c "" is falsy

#=========================
# Common mistakes to avoid
#=========================


# '=' vs. '=='
# '=' is assignment, '==' is comparison.
if x = 5:    # ❌ SyntaxError
if x == 5:   # ✅ comparison


# Forgetting the colon ':'
if x > 3     # ❌
if x > 3:    # ✅


# Inconsistent indentation (mixing tabs/spaces). Stick to 4 spaces.
# Comparing different types accidentally (e.g., string "5" vs int 5). Convert:
age_str = "20"
age = int(age_str)    # now it's a number


#==============
# Mini examples
#==============

# Example 1: Grade classifier
# ---------------------------

score = 83

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# Example 2: Even or odd
# ----------------------

n = 7

if n % 2 == 0:
    print("Even")
else:
    print("Odd")
# Remember, % is modulo(remainder). If the remainder of n/2 equals 0, it's even.


# Example 3: Simple login check
# -----------------------------

username = "alice"
passwd = "secret"

if username == "alice" and passwd == "secret":
    print("Welcome!")
else:
    print("Invalid credentials")
