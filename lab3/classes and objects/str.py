# The __str__() Function

# The string representation of an object WITHOUT the __str__() function:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Jonh", 37)

print(p1)

# The string representation of an object WITH the __str__() function:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"
p1 = Person("Jonh", 37)

print(p1)
        
        
        