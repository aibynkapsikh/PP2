import re

def split_by_uppercase(s):
    return re.findall(r"[A-Z][a-z]*", s)

test_strings = [
    "HelloWorldPython",  
    "SplitThisString",   
    "OneTwoThree",     
    "NoUppercase",      
    "lowercaseonly"     
]

for s in test_strings:
    print(f"{s} → {split_by_uppercase(s)}")
