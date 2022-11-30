from bank import bank_program
from Console_file_manager_functions import create_folder, delete_folder, copy_folder_or_file, show_files_and_folders, show_folders, show_files, system_info, change_directory, creator
from victory import victory

while True:
    print('')
    print('1. создать папку')
    print('2. удалить папку')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. смена рабочей директории')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. создатель программы')
    print('12. выход')

    choice = input('Выберите пункт меню\n')
    if choice == '1':
        folder_name = input('введите название папки\n')
        create_folder(folder_name)

    elif choice == '2':
        folder_name = input('введите название папки\n')
        delete_folder(folder_name)

    elif choice == '3':
        file_name = input('введите название файла или папки\n')
        fpath = f'C:/Users/Роман/PycharmProjects/консольный_файловый_менеджер/{file_name}'
        folder_name = input('введите новое название\n')
        copy_folder_or_file(fpath, file_name, folder_name)

    elif choice == '4':
        show_files_and_folders()

    elif choice == '5':
        show_folders()

    elif choice == '6':
        show_files()

    elif choice == '7':
        system_info()

    elif choice == '8':
        change_directory()

    elif choice == '9':
        victory()

    elif choice == '10':
        bank_program()

    elif choice == '11':
        creator()

    elif choice == '12':
        break

    else:
        print('Неверный пункт меню')
