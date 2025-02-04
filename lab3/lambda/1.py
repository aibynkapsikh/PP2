# Lambda

# A lambda function can take any number of arguments, but can only have one expression.

# Syntax 
# lambda arguments : expression

x = lambda a : a + 10
print(x(5))

# Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

# Summarize argument 
x = lambda a, b, c : a + b + c
print(x(3, 2, 4))

# Example function

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(3)

print(mydoubler(2))

# Use lambda functions when an anonymous function is required for a short period of time.
