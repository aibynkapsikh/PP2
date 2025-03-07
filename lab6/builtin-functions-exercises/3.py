from functools import reduce
import math
import time

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar")) 
print(is_palindrome("hello")) 


