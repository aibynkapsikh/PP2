# One more value, or object in this case, evaluates to False, and that is if you have an object
#  that is made from a class with a __len__ function that returns 0 or False:

# Example

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


# Functions can Return a Boolean
# We can create functions that returns a Boolean Value:

def myFunction() :
  return True

print(myFunction())

# We can execute code based on the Boolean answer of a function:

# Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# We also can use built-in functions such as - isinstance()

# Check if an object is an integer or not:

x = 200
print(isinstance(x, int)) 