# Creating a Function
# In Python a function is defined using the def keyword:

def my_function():
    print("Hello from a function")

my_function()

# Arguments

def my_function(fname):
    print(fname + "Refsnes")

my_function("Emil")
my_function("Aibyn")


# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# Number of Arguments

# This function expects 2 arguments, and gets 2 arguments:

def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Aibyn", "Kapsikh") # If you try to call the function with 1 or 3 arguments, you will get an error:


# Arbitrary Arguments, *args

# If the number of arguments is unknown, add a * before the parameter name:

def my_function(*child):
    print("The youngest child is " + child[1])

my_function("Linus", "Tobias", "Emil")


