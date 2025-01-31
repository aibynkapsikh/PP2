# Dictionaries

# Dictionaries are used to store data values in key:value pairs.

thisdict = {
    "Name" : "Aibyn",
    "Age" : 17,
    "Speciality" : "Information System"
}

print(thisdict)
print(thisdict["Age"])

# Duplicates Not Allowed

thisdicts = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964, # Dictionaries cannot have two items with the same key:
  "year": 2020
}
print(thisdicts)

# Dictionary Length
print(len(thisdict))

# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:

dict_1 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# Type
print(type(thisdict))


# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.

dict_2 = dict(name = "Aibyn", age = 17, country = "Kazakhstan")
print(dict_2)