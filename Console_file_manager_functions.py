import os
import shutil
import sys


def create_folder(folder_name):
    '''
    Создать папку
    '''
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        print('Такая папка уже существует')


def delete_folder(folder_name):
    '''
    Удалить (папку)
    '''
    try:
        os.rmdir(folder_name)
    except FileNotFoundError:
        print('Такой попки не существует')


def copy_folder_or_file(fpath, file_name, folder_name):
    '''
    Копировать (файл/папку)
    '''
    try:
        if os.path.isdir(fpath):
            shutil.copytree(file_name, folder_name, copy_function=shutil.copy)

        else:
            shutil.copy(file_name, folder_name)
    except FileNotFoundError:
        print('Такой попки или файла не существует')


def show_files_and_folders():
    '''
    Просмотр содержимого рабочей директории
    '''
    print(os.listdir())


def save_files_and_folders():
    files_and_folders_list = os.listdir()
    folder_path = os.getcwd() + '/'

    files_list = [i for i in files_and_folders_list if os.path.isfile(folder_path + i)]

    folders_list = [i for i in files_and_folders_list if os.path.isdir(folder_path + i)]

    files_and_folders = open("listdir.txt", "w")
    files_and_folders.write(f'files: {files_list}\n dirs: {folders_list}')
    files_and_folders.close()


def show_folders():
    '''
    Посмотреть только папки
    '''

    files_and_folders_list = os.listdir()
    folder_path = os.getcwd() + '/'

    folders_list = [i for i in files_and_folders_list if os.path.isdir(folder_path + i)]

    print(folders_list)


def show_files():
    '''
    Посмотреть только файлы
    '''

    files_and_folders_list = os.listdir()
    folder_path = os.getcwd() + '/'

    files_list = [i for i in files_and_folders_list if os.path.isfile(folder_path + i)]

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
