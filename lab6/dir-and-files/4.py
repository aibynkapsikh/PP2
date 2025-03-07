import os
import shutil

def count_lines(file_path):
    with open(file_path, "r") as f:
        return sum(1 for _ in f)

print(count_lines("test.txt"))

