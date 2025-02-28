 # Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

def match_pattern(s):
    pattern = r'a*b*'
    return bool(re.fullmatch(pattern, s))

test_strings = ["a", "ab", "abb", "aabb", "b", "bb", "aaa", "abc"]

for s in test_strings:
    print(f"{s}: {match_pattern(s)}")