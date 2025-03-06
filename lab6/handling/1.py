# Python File Open
# Syntax
# To open a file for reading it is enough to specify the name of the file:

f = open("test.txt")

t = open("test.txt", "rt")

# Note: Make sure the file exists, or else you will get an error.

# Open a File on the Server
# Assume we have the following file, located in the same folder as Python:

f = open("test.txt", "r")
print(f.read())

# Open a file on a different location:

# f = open("C:\Users\user\OneDrive\Desktop\code\labs\lab6\handling\test.txt", "r")
# print(f.read())


# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

# 
# Example

f = open("test.txt", "r")
print(f.read(5))

# Read Lines
# You can return one line by using the readline() method:

# Example
# Read one line of the file:

f = open("test.txt", "r")
print(f.readline()) # By calling readline() two times, you can read the two first lines:


# Loop through the file line by line:

f = open("test.txt", "r")
for x in f:
  print(x)

# Close Files
# It is a good practice to always close the file when you are done with it.

f = open("test.txt", "r")
print(f.readline())
f.close()