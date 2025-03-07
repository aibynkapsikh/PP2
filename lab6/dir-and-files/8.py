import os
import shutil

def delete_file(file_path):
    if os.path.exists(file_path) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"Deleted {file_path}")
    else:
        print("File not found or no permission to delete")

delete_file("copy_test.txt")
