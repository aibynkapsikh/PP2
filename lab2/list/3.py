# Loop Through the Index Numbers

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


# Using a While Loop

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


# List Comprehension

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for x in fruits:
  if "a" in x:
    new_list.append(x)

print(new_list)