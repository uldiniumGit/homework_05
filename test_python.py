import math
'''
Тесты для встроенных функций filter, map, sorted
'''


# функция для фильтрации
def list_filter(your_list):
    if isinstance(your_list, int):
        return True
    else:
        return False


# возведение в квадрат
def square(number):
    return number ** 2


# тест для встроенной функции filter
def test_filter():
    list_for_filter = [1, 2, 4, 5, 7, 8, 10, 11, 'abc']
    list_after_filtration = list(filter(list_filter, list_for_filter))
    assert list_after_filtration == [1, 2, 4, 5, 7, 8, 10, 11]


# тест для встроенной функции map
def test_map():
    list_for_map = [1, 2, 3, 4, 5]
    list_after_mapping = list(map(square, list_for_map))
    assert list_after_mapping == [1, 4, 9, 16, 25]


# тест для встроенной функции sorted
def test_sorted():
    list_for_sorted = [3, 2, 1]
    list_after_sorting = sorted(list_for_sorted)
    assert list_after_sorting == [1, 2, 3]


'''
Тесты для встроенных функций  pi, sqrt, pow, hypot из библиотеки math
'''


def test_pi():
    assert math.pi == 3.141592653589793


def test_sqrt():
    assert math.sqrt(4) == 2


def test_pow():
    assert math.pow(2, 2) == 4


def test_hypot():
    assert math.hypot(3, 4) == 5.0
