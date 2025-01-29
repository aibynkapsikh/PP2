# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.
print(bool("abc"))
print(bool(""))

# Any number is True, except 0.
print(bool(0))
print(bool(1234))

# Any list, tuple, set, and dictionary are True, except empty ones.

print(bool(["apple", "cherry", "banana"]))
print(bool([]))