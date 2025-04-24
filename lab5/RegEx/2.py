# # Match Object

# A Match Object is an object containing information about the search and the result.


import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object


# .span() returns a tuple containing the start-, and end positions of the match.

x = re.search(r"\bS\w+", txt)
print(x.span())

# .string returns the string passed into the function

x = re.search(r"\bS\w+", txt)
print(x.string)

# .group() returns the part of the string where there was a match

x = re.search(r"\bS\w+", txt)
print(x.group())

# Note: If there is no match, the value None will be returned, instead of the Match Object.


