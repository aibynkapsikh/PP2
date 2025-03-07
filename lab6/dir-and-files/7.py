import os
import shutil

def copy_file(src, dest):
    shutil.copy(src, dest)

copy_file("test.txt", "copy_test.txt")

