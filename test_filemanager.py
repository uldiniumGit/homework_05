import os
from Console_file_manager_functions import create_folder, delete_folder, copy_folder_or_file
from bank_functions import donate, buy
from victory import check_answer

'''
Тесты для функций банка
'''


def test_donate():
    assert donate(0, 100) == 100
    assert donate(100, 100) == 200


def test_buy():
    purchase_dict = {}
    balance = 100
    price = 20
    purchase = 'abc'
    balance, purchase_dict = buy(balance, price, purchase, purchase_dict)
    assert balance == 80
    assert purchase_dict == {'abc': 20}


'''
Тесты для функций викторины
'''


def test_check_answer():
    assert check_answer(1, 1) == 1
    assert check_answer(1, 2) == 0


'''
Тесты для функций консольного файлового менеджера
'''


def test_create_and_delete_folder():
    if os.path.isdir(os.getcwd() + '/abc'):
        assert False, 'такая папка уже существует, замените название папки в тесте'
    folder_name = 'abc'
    create_folder(folder_name)
    assert os.path.isdir(os.getcwd() + '/abc')
    delete_folder(folder_name)
    assert os.path.isdir(os.getcwd() + '/abc') is False


def test_copy_folder_or_file():
    if os.path.isdir(os.getcwd() + '/abc'):
        assert False, 'такая папка уже существует, замените название папки в тесте'
    if os.path.exists(os.getcwd() + '/123'):
        assert False, 'такой файл уже существует, замените название файла в тесте'

    os.mkdir('abc')
    copy_folder_or_file('C:/Users/Роман/PycharmProjects/консольный_файловый_менеджер/abc', 'abc', 'abcd')
    assert os.path.isdir(os.getcwd() + '/abcd')
    os.rmdir('abc')
    os.rmdir('abcd')

    my_file = open("123", "a+")
    my_file.close()
    copy_folder_or_file('C:/Users/Роман/PycharmProjects/консольный_файловый_менеджер/123', '123', '1234')
    assert os.path.exists(os.getcwd() + '/1234')
    os.remove('123')
    os.remove('1234')
