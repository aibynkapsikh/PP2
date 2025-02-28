import re

def camel_to_snake(s):
    return re.sub(r'([A-Z])', r'_\1', s).lower().lstrip("_")

test_strings = [
    "HelloWorld",      
    "ConvertMeNow",    
    "ThisIsATest",     
    "Already_Snake",   
    "lowercaseonly"    
]

for s in test_strings:
    print(f"{s} → {camel_to_snake(s)}")
