# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
# cp <file_name> - создает копию указанного файла
# rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
# cd <full_path or relative_path> - меняет текущую директорию на указанную
# ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> (первый параметр) - создание директории")
    print("cp <file_name> (второй параметр) - удаляет указанный файл")
    print("cd <full_path> (третий параметр) - замена текущей директории на указанную ")
    print("ls - отображение полного пути текущей директории")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def cp():
    if not file_name:
        print("Необходимо указать имя удаляемого файла третьим параметром")
        return
    dir_path = os.path.join(os.getcwd(), file_name)
    try:
        print("Подтвердите удаление файла! 1 - подтвердить, другое - нет")
        answer = input()
        if answer == "1":
            os.remove(file_name)
            print('файл с именем {} удален успешно'.format(file_name))
    except FileNotFoundError:
        print('файла с именем {} не существует'.format(file_name))

def cd():
    if not full_path:
        print("Необходимо указать путь до папки четвертым параметром")
        return
    try:
        os.chdir(full_path)
        print("Переход в папку ", os.getcwd() , " выполнен успешно" )
    except FileNotFoundError:
        print ("Такой директории не существует")

def ls():
    print("Текущая директория: ", os.getcwd())


import os, sys
do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp": cp,
    "cd": cd,
    "ls": ls
}
cont = 0
try:
    key = sys.argv[1]
except IndexError:
    key = None
try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None
try:
    file_name = sys.argv[3]
except IndexError:
    file_name = None
try:
    full_path = sys.argv[4]
except IndexError:
    full_path = None

while cont != "1":
    if key == None:
        print_help()
        answer = input()
        new_key = answer.split()
        key = new_key[0]
        try:
            dir_name = new_key[1]
        except IndexError:
            dir_name = None
        try:
            file_name = new_key[2]
        except IndexError:
            file_name = None
        try:
            full_path = new_key[3]
        except IndexError:
            full_path = None

    else:
        if do.get(key):
            do[key]()
        else:
            print_help
            print("Задан неверный ключ")
            print("Укажите ключ help для получения справки")
        print ("1 - Завершить, Другое - Продолжить")
        cont = input()
        key = None
