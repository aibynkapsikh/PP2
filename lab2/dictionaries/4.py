# Remove Dictionary Items

# There are several methods to remove items from a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# The pop() method removes the item with the specified key name:
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name:

del thisdict["model"]
print(thisdict)

# The del keyword can also delete the dictionary completely:
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

# The clear() method empties the dictionary:
thisdict.clear()
print(thisdict)