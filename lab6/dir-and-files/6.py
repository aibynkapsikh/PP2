import os
import shutil

def create_alphabet_files():
    for char in range(65, 91): 
        with open(f"{chr(char)}.txt", "w") as f:
            f.write(f"This is {chr(char)}.txt\n")

create_alphabet_files()
