from functools import reduce
import math
import time

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

print(multiply_list([1, 2, 3, 4])) 


