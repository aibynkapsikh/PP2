print(10 > 9) # True
print(10 == 9) # False
print(10 < 9) # False

# When you run a condition in an if statement, Python returns True or False


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# The bool() function allows you to evaluate any value, and give you True or False in return
# Any number is True, except 0
print(bool("Hello")) # True
print(bool(0)) # False 

x = "Hello"
y = 15

print(bool(x)) # True
print(bool(y)) # True
