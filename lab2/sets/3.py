# Loop sets

# Loop through the set, and print the values:

first_set = {"apple", "banana", "cherry", "pineapple"}

for x in first_set:
    print(x)

# Join Sets

# There are several ways to join two or more sets in Python.

# Union

# The union() method returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# You can use the | operator instead of the union() method, and you will get the same result.

set_3 = set1 | set2
print(set_3)

# Update

# The update() method inserts all items from one set into another.

set1.update(set2)
print(set1)