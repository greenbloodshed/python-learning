#==============================================================================================================
# Boolean Values
#==============================================================================================================

# In programming you often need to know if an expression is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.
# When you compare two values, the expression is evaluated and Python returns the Boolean answer:

# Example 1
print(10 > 9)
print(10 == 9)
print(10 < 9)
#(Outputs: True, False, False)


# Example 2 - When you run a condition in an if statement, Python returns True or False:
A = 200
B = 33

if B > A:
    print("B is greater than A")
else:
    print("B is not greater than A")
        #(Outputs: B is not greater than A)

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return.

# Example 3
# Evaluate a string and a number w/ bool():
print(bool("Hello"))
print(bool(15))
#(Outputs: True, True)

# Example 4
# Evaluate two variables w/ bool():
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
#(Outputs: True, True)

#===========================
# Most Values are True
#===========================
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

# Example 5
# The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#===========================
# Some Values are False
#===========================
# There are not many values that evaluate to False.
# Empty values, such as (), [], {}, "", the number 0, and the value None evaluate to False.
# The value False evaluates to False.

# The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

'''
One more value, or object in this case, evaluates to False, and that is if you have an object
that is made from a class with a __len__ function that returns 0 or False:
'''

# Example
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#================================
# Functions can Return a Boolean
#================================

# You can create functions that returns a Boolean Value:

# Example
def myFunction() :
   return True

print(myFunction())

# You can execute code based on the Boolean answer of a function:

# Example
# Print "YES!" if the function returns True, otherwise print "NO!":
if myFunction():
   print("YES!")
else:
   print("NO!")

'''
Python also has many built-in functions that return a boolean value, like the
isinstance() function, which can be used to determine if an object is of a certain data type:
'''

# Example
# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))
