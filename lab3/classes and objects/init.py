# Classes and Objects

# A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a class 

class MyClass:
    x = 5

# Create Object
# we can use the class named MyClass to create objects:

p1 = MyClass
print(p1.x)

# The __init__() Function

class Person:
    def __init__(self, name, age): # Note: The __init__() function is called automatically every time the class is being used to create a new object.
        self.name = name
        self.age = age

p1 = Person("Aibyn", 17)

print(p1.name)
print(p1.age)        

