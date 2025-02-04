# Inheritance

# Create a Parent Class

# Any class can be a parent class, so the syntax is the same as creating any other class:

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname) 
#Use the Person class to create an object, and then execute the printname method
x = Person("Jonh","Liar")
x.printname()

# Create a Child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

class Student(Person):
    pass # Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

x = Person("Mike", "Doe")
x.printname()



        