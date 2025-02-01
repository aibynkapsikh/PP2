# Keyword Arguments

# You can also send arguments with the key = value syntax.

def my_function(child3, child2, child1):
    print("The youngest child is " + child2)

my_function(child3 = "Emil", child2 = "Linus", child1 = "Tobias")

# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

def my_function(**kid):
    print("The youngest child is " + kid["fname"])

my_function(fname = "Linus", lname = "Refsnes")

# Default Parameter Value

def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Brazil")
my_function("Canada")
my_function()
my_function("Kazakhstan")


# Passing a List as an Argument

def my_function(food):
    for x in food:
        print(x)

my_list = ['apple', 'banana', 'cherry']

my_function(my_list)

# Return Values
# To let a function return a value, use the return statement:

def my_function(value):
    return value * 5

print(my_function(3))
print(my_function(9))
print(my_function("Hello "))

# The pass Statement
def myfunction():
  pass # having an empty function definition like this, would raise an error without the pass statement

# Positional-Only Arguments

def my_function(name, /):
    print(name)

my_function("Aibyn")

# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

def my_function(x):
  print(x)

my_function(x = 3)

# But when adding the , / you will get an error if you try to send a keyword argument:
def my_function(x, /):
  print(x)

my_function(x = 3) # Error

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:

def my_function(*, x):
   print(x)

my_function(x = 4)

# Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:
def my_function(x):
  print(x)

my_function(3)

# But with the *, you will get an error if you try to send a positional argument:

def my_function(*, x):
  print(x)

my_function(3) # Error

def my_function(x, y, /, *, z, w):
   print(x + y + z + w)

my_function(3, 7, z = 10, w = 10)

# Recursion
# Python also accepts function recursion, which means a defined function can call itself.

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)