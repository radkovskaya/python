# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
def add_dir():
    print("Введите имя новой папки")
    name = input()
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
        print ("Директория создана, имя новой директории - ", name)
    except FileExistsError:
        print('Такая директория уже существует')

def remove_dir():
    print("Введите имя папки для удаления")
    name = input()
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.rmdir(dir_path)
        print("Директория удалена, имя директории - ", name)
    except FileNotFoundError:
        print("Такой директории не существует")

#add_dir()
#remove_dir()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def show_folders():
    print("Список папок в текущей директории: ")
    for element in os.listdir(os.getcwd()):
        if os.path.isdir(element):
            print(element)

# Вызов функции:
# show_folders()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import sys
import shutil
def copy_file(name):
    name_file = name + ".py"
    copy = os.path.join(os.getcwd(), name_file)
    shutil.copyfile(sys.argv[0], copy)
    print("Текущий файл скопирован в файл с именем ", name_file)

#copy_file("name")