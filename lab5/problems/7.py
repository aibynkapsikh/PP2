import re

def snake_to_camel(s):
    return "".join(word.capitalize() for word in s.split("_"))

test_strings = [
    "hello_world",      
    "convert_me_now",   
    "this_is_a_test",   
    "alreadyCamel"       
]

for s in test_strings:
    print(f"{s} → {snake_to_camel(s)}")
