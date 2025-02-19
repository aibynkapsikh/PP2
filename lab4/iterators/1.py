# Iterators

# An iterator is an object that contains a countable number of values.

# All these objects have a iter() method which is used to get an iterator:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myiit = iter(mystr)

print(next(myiit))
print(next(myiit))
print(next(myiit))
print(next(myiit))
print(next(myiit))
print(next(myiit))

# Looping Through an Iterator

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)


mystr = "banana"

for x in mystr:
  print(x) # The for loop actually creates an iterator object and executes the next() method for each loop.





