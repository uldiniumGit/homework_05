import os
import shutil
import sys


def create_folder():
    '''
    Создать папку
    '''
    folder_name = input('введите название папки\n')
    os.mkdir(folder_name)


def delete_folder():
    '''
    Удалить (файл/папку)
    '''
    folder_name = input('введите название папки\n')
    os.rmdir(folder_name)


def copy_folder_or_file():
    '''
    Копировать (файл/папку)
    '''
    file_name = input('введите название файла\n')
    fpath = f'C:/Users/Роман/PycharmProjects/консольный_файловый_менеджер/{file_name}'
    if os.path.isdir(fpath):
        folder_name = input('введите новое название\n')
        shutil.copytree(file_name, folder_name, copy_function=shutil.copy)
    else:
        folder_name = input('введите новый путь\n')
        shutil.copy(file_name, folder_name)


def show_files_and_folders():
    '''
    Просмотр содержимого рабочей директории
    '''
    print(os.listdir())


def show_folders():
    '''
    Посмотреть только папки
    '''
    files_and_folders_list = os.listdir()
    folders_list = []
    folder_path = f'C:/Users/Роман/PycharmProjects/консольный_файловый_менеджер/'
    for i in files_and_folders_list:
        if os.path.isdir(folder_path + i):
            folders_list.append(i)
    print(folders_list)


"""
Более короткий вариант
folders_list_another = [f.path for f in os.scandir('.') if f.is_dir()]
print(folders_list_another)
"""


def show_files():
    '''
    Посмотреть только файлы
    '''
    files_and_folders_list = os.listdir()
    files_list = []
    folder_path = f'C:/Users/Роман/PycharmProjects/консольный_файловый_менеджер/'
    for i in files_and_folders_list:
        if os.path.isfile(folder_path + i):
            files_list.append(i)
    print(files_list)


def system_info():
    '''
    Просмотр информации об операционной системе
    '''
    print('My OS is', sys.platform, '(', os.name, ')')


def creator():
    '''
    Создатель программы
    '''
    uldinium = open('uldinium')
    print(uldinium.read())


def change_directory():
    '''
    Смена рабочей директории
    '''
    new_dir = input('введите новую директорию')
    os.chdir(new_dir)
