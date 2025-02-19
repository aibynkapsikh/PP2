# Global Keyword

# The global keyword makes the variable global.

def myfunc():
    global x
    x = 300

myfunc()
print(x)


x = 300
def myfunc():
    global x
    x = 200

myfunc()

print(x)

# Nonlocal keyword

# If you use the nonlocal keyword, the variable will belong to the outer function:

def myfunc1():
    x = "Aibyn"
    def myfunc2():
        nonlocal x
        x = "AIBYN"
    myfunc2()
    return x

print(myfunc1())
