import re 

def match_pattern(s):
    pattern = r'ab{2, 3}'
    return bool(re.fullmatch(pattern, s))

test_strings = ["abb", "abbb", "ab", "a", "abbbb"]
for s in test_strings:
    print(f"{s}: {match_pattern(s)}")