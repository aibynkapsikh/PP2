# Sets are used to store multiple items in a single variable.

#  Note: Set items are unchangeable, but you can remove items and add new items.

# Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset) # Note: Sets are unordered, so you cannot be sure in which order the items will appear.


# Duplicates Not Allowed
 
myset = {"apple", "banana", "cherry", "apple"}

print(myset) # Duplicate values will be ignored:

# True and 1
# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

set_1 = {"apple", "banana", "cherry", True, 1, 2} # True and 1 is considered the same value:

print(set_1) 

# False and 0

set_2 = {"apple", "banana", "pineapple", False, 0, 2} # False and 0 is considered the same value:

print(set_2)

# Add Items
# To add one item to a set use the add() method.
thisset.add("orange")

print(thisset)

# To add items from another set into the current set, use the update() method.
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)