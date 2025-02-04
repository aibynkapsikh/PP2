# Object Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("My name is " + self.name) # Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

p1 = Person("Aibyn", 17)
p1.myfunc()

# The self Parameter

# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:

# Example
# Use the words mysillyobject and abc instead of self:

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("My name is " + abc.name)

p1 = Person("Aibyn", 17)
p1.myfunc()

# Modify Object Properties

# You can modify properties on objects like this:
p1.age = 40

# Delete Object Properties

del p1.age

# Delete Objects
del p1

# The pass Statement
class Person:
    pass