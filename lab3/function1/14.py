# my_functions.py
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
