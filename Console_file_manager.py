from bank import bank_program
from Console_file_manager_functions import create_folder, delete_folder, copy_folder_or_file, show_files_and_folders, \
    show_folders, show_files, save_files_and_folders, system_info, change_directory, creator
from victory import victory

while True:
    print('')
    print('1. создать папку')
    print('2. удалить папку')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. сохранить содержимое рабочей директории в файл ')
    print('6. посмотреть только папки')
    print('7. посмотреть только файлы')
    print('8. просмотр информации об операционной системе')
    print('9. смена рабочей директории')
    print('10. играть в викторину')
    print('11. мой банковский счет')
    print('12. создатель программы')
    print('13. выход')

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
        save_files_and_folders()

    elif choice == '6':
        show_folders()

    elif choice == '7':
        show_files()

    elif choice == '8':
        system_info()

    elif choice == '9':
        change_directory()

    elif choice == '10':
        victory()

    elif choice == '11':
        bank_program()

    elif choice == '12':
        creator()

    elif choice == '13':
        break

    else:
        print('Неверный пункт меню')
