# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
def add_dir():
    i = 1
    while i < 10:
        j = str(i)
        dir = "dir_" + j
        dir_path = os.path.join(os.getcwd(), dir)
        try:
            os.mkdir(dir_path)
            print ("Директория создана")
        except FileExistsError:
            print('Такая директория уже существует')
        i +=1

def remove_dir():
    i = 1
    while i < 10:
        j = str(i)
        dir = "dir_" + j
        dir_path = os.path.join(os.getcwd(), dir)
        try:
            os.rmdir(dir_path)
            print("Директория удалена")
        except FileNotFoundError:
            print("Такой директории не существует")
        i +=1

# Вызовы функций:
# add_dir()
# remove_dir()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def show_folders():
     for element in os.listdir(os.getcwd()):
        if os.path.isdir(element):
           print(element)

# Вызов функции:
# show_folders()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import sys
import shutil
def copy_file():
    copy = os.path.join(os.getcwd(), "new.py")
    shutil.copyfile(sys.argv[0], copy)
    print("Файл скопирован в файл с именем new")

# Вызов функции:
# copy_file()
