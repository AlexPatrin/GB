# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
def create_folder():
    lists = []
    print('Содержимое папки: ')
    for _ in range(1, 10):
        path = f'{os.getcwd()}\dir{_}'
        lists.append(path)
        print(path)
        os.mkdir(path)
    print('----------------------')
    return lists
# lse = create_folder()
# print(lse)
# input('Нажми Enter для продолжения')

def delete_folder(lf):
    for i in lf:
        os.rmdir(i)
# delete_folder(lse)


def cr_folder(fn):
    try:
        path = f'{os.getcwd()}\{fn}'
        os.mkdir(path)
    except OSError:
        print('Создать директорию %s не удалось\n' % fn)
    else:
        print('Успешно создана директория %s\n' % fn)

def del_folder(ls):
    try:
        os.rmdir(ls)
    except OSError:
        print('Удалить директорию %s не удалось\n' % ls)
    else:
        print('Успешно удалена директория %s\n' % ls)
# del_folder(ls)

def mv_folder(fn):
    try:
        path = f'{os.getcwd()}\{fn}'
        os.chdir(path)
    except OSError:
        print('Невозможно перейти в директорию %s\n' % fn)
    else:
        print('Успешно перешли в директорию %s\n' % fn)




# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
from os.path import isdir
def lis_folder():
    for i in os.listdir():
        if isdir(i):
            print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
def copy_s():
    name = os.path.basename(__file__)
    shutil.copy(__file__, f'{os.getcwd()}\copy_{name}')

