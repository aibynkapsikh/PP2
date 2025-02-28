import re

def insert_spaces(s):
    return re.sub(r"([A-Z])", r" \1", s).strip()

test_strings = [
    "HelloWorldPython", 
    "InsertSpacesHere", 
    "OneTwoThree",      
    "NoSpacesNeeded",   
    "lowercaseonly"    
]

for s in test_strings:
    print(f"{s} → {insert_spaces(s)}")
