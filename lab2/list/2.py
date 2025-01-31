# List items are indexed and you can access them by referring to the index number:

mylist = ["apple", "banana", "cherry"]
print(mylist[1]) # Note: The first item has index 0

# Negative Indexing
print(mylist[-1])

# Range of Indexes

# You can specify a range of indexes by specifying where to start and where to end the range.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # "cherry", "orange", "kiwi"
# Note: The search will start at index 2 (included) and end at index 5 (not included).

# Check if Item Exists

# To determine if a specified item is present in a list use the in keyword:

# Check if "apple" is present in the list:

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

