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


# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist_1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist_1.sort()
print(thislist_1)

# Sort the list numerically:

thislist_2 = [100, 50, 65, 82, 23]
thislist_2.sort()
print(thislist_2)

# Sort Descending
# To sort descending, use the keyword argument reverse = True:
thislist_1.sort(reverse = True)
print(thislist_1)
