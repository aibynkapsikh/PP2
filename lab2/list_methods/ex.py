# Python has a set of built-in methods that you can use on lists.

# Method : append
# Description : Adds an element at the end of the list

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

# Method : clear
# Description : Removes all the elements from the list
fruits.clear()

# Method : count
# Description : Returns the number of elements with the specified value
x = fruits.count("cherry")
print(x)

# Method : insert
# Description : Adds an element at the specified position
fruits.insert(1, "orange")
print(fruits)

# Method : pop
# Description : Removes the element at the specified position
fruits.pop(1)

# Method : remove
# Description : Removes the item with the specified value
fruits.remove("banana")

# Method : reverse
# Description : Reverses the order of the list
fruits.reverse()

# Method : sort
# Discription : Sorts the list
fruits.sort()

