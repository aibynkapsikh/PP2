# Accessing Items

# You can access the items of a dictionary by referring to its key name, inside square brackets:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

# There is also a method called get() that will give you the same result:
x = thisdict.get("model")
print(x)

# Get keys

x = thisdict.keys()
print(x)

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

x = car.keys() # before change

car["color"] = "white"

print(x) # after change

# Get values
# The values() method will return a list of all the values in the dictionary.

x = thisdict.values()

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()



