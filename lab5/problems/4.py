import re

def find_upper_lower(text):
    pattern = r"[A-Z][a-z]+"
    return re.findall(pattern, text)

test_strings = [
    "Hello",
    "World",
    "Python",
    "ccC",
    "JAVA",
    "java",
    "Test"
]

for s in test_strings:
    print(f"{s}: {find_upper_lower(s)}")