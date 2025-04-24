
# Python RegEx

import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")


# RegEx Functions
# The re module offers a set of functions that allows us to search a string for a match
# The findall() Function
# The findall() function returns a list containing all matches.

x = re.findall("ai", txt)
print(x)

# The search() Function

x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


# The split() Function

x = re.split("\s", txt)
print(x)

# 
#The sub() Function

x = re.sub("\s", "9", txt)
print(x)

