import os
import shutil

def write_list_to_file(file_path, data):
    with open(file_path, "w") as f:
        for item in data:
            f.write(str(item) + "\n")

write_list_to_file("output.txt", ["apple", "banana", "cherry"])
