import re

def replace_symbols(text):
    pattern = r"[ ,.]" 
    return re.sub(pattern, ":", text)

test_strings = [
    "Hello, world. How are you?",  
    "Python is great, isn't it.",  
    "No symbols here"  
]

for s in test_strings:
    print(f"Before: {s}")
    print(f"After:  {replace_symbols(s)}\n")
