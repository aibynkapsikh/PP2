# The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits 

print(green)
print(yellow)
print(red)

# Loop Through the Index Numbers

mytuple = ("apple", "banana", "cherry")
for i in range(len(mytuple)):
  print(mytuple[i])

# Join two tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:

mytuple = fruits * 2
print(mytuple)
