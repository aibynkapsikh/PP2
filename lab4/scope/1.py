# Scope

# A variable is only available from inside the region it is created. This is called scope.

# Local Scope

# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def myfunc():
    x = 300
    print(x)

myfunc()

# Function Inside Function


def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()


# Global Scope

# A variable created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
    print(x)

myfunc()

print(x)

# Naming Variables

# The function will print the local x, and then the code will print the global x:
x = 300

def myfunc():
    x = 200
    print(x)

myfunc()

print(x)
