# Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)

# Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Looping Through a String

for x in "banana":
  print(x)  

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:

for x in fruits:
  print(x)
  if x == "banana":
    break

# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:

for x in fruits:
  if x == "banana":
    continue
  print(x)

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,

for x in range(6):
  print(x)

# Using the start parameter:

for x in range(2, 6):
  print(x)

# Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)
