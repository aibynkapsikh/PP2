import re

def find_sequences(text):
    pattern = r"\b[a-z]+_[a-z]+\b"
    return re.findall(pattern, text)

test_strings = [
    "hello_world",
    "snake_case",
    "HEllo_Wolrd",
    "test123_test",
]

for s in test_strings:
    print(f"{s}: {find_sequences(s)}")
    