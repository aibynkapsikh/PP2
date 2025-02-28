import re

def match_pattern(s):
    pattern = r"a.*b$"  
    return bool(re.fullmatch(pattern, s))

test_strings = [
    "axb",      
    "acb",      
    "ab",        
    "a123b",     
    "abc",       
    "b",         
    "a_something_b" 
]

for s in test_strings:
    print(f"{s}: {match_pattern(s)}")
