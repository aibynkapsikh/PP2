import os
print(os.getcwd())


# Если нужно переключиться в другую папку:

os.chdir("C:/Users/Username/Desktop")
print(os.getcwd())


# Посмотреть файлы и папки в текущей директории:
print(os.listdir())  # Покажет файлы и папки в текущей директории
print(os.listdir("C:/Users/Username/Desktop"))


# 🔹 5. Создание папки

os.mkdir("new_folder")

# Удаление папки

os.rmdir("new_folder")

# Удаление папки с файлами

import shutil
shutil.rmtree("pattern_folder")

# Проверка существования папки

if os.path.exists("new_folder"):
    os.rmdir("new_folder")
else:
    print("Папка не найдена!")

# Переименование папки
os.rename("old_folder", "new_folder")

