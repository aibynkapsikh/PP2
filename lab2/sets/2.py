# Remove Set Items

# To remove an item in a set, use the remove(), or the discard() method.

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana") # Note: If the item to remove does not exist, remove() will raise an error.

print(thisset)

thisset.discard("banana") # Note: If the item to remove does not exist, discard() will NOT raise an error.

print(thisset)

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

# The return value of the pop() method is the removed item.

x = thisset.pop()

print(x)

print(thisset)

# Clear method
thisset.clear()

print(thisset) # The clear() method empties the set: