# Create a Module

# To create a module just save the code you want in a file with the file extension .py:

def greeting(name):
    print("Hello, " + name)

import mymodule

mymodule.greeting("Aibyn") # Note: When using a function from a module, use the syntax: module_name.function_name.

# Variables in Module

person1 = {
    "name": "Aibyn",
    "age": 18,
    "country": "Kazakhstan"
}

import mymodule

a = mymodule.person1["age"]
print(a)


# Naming a Module
# We can name the module file whatever you like, but it must have the file extension .py

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:

import mymodule as mx

a = mx.person1["age"]
print(a)


# Built-in Modules

import platform

x = platform.system()
print(x)

# Using the dir() Function

x = dir(platform) # Note: The dir() function can be used on all modules, also the ones you create yourself.
print(x)

# Import From Module
# You can choose to import only parts from a module, by using the from keyword.

from mymodule import person1

print (person1["age"])