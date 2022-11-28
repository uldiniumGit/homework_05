import random

# Словарь для перевода даты из формата '01.01.2000' в формат 'первое января 2000 года'
dict_dates = {'27.01.1756': 'двадцать седьмое января 1756 года', '21.03.1685': 'двадцать первое марта 1685 года',
              '04.03.1678': 'четвертое марта 1678 года', '15.06.1843': 'пятнадцатое июня 1843 года',
              '22.10.1811': 'двадцать второе октября 1811 года', '31.01.1797': 'тридцать первое января 1797 года',
              '16.12.1770': 'шестнадцатое декабря 1770 года', '18.08.1750': 'восемнадцатое августа 1750 года',
              '07.05.1840': 'седьмое мая 1840 года', '22.05.1813': 'двадцать второе мая 1813 года'}


# Функция для проверки ответа
def check_answer(answer, correct_answer):
    if answer == correct_answer:
        return 1
    else:
        print('Неверно. Правильная дата рождения:', dict_dates[correct_answer], '\n')
        return 0


def victory():
    # Правильные ответы для каждой знаменитости
    mozart_birthday_year = '27.01.1756'
    bach_birthday_year = '21.03.1685'
    vivaldi_birthday_year = '04.03.1678'
    grieg_birthday_year = '15.06.1843'
    liszt_birthday_year = '22.10.1811'
    schubert_birthday_year = '31.01.1797'
    beethoven_birthday_year = '16.12.1770'
    salieri_birthday_year = '18.08.1750'
    tchaikovsky_birthday_year = '07.05.1840'
    wagner_birthday_year = '22.05.1813'

    # Цикл с викториной
    while True:
        # Переменная для подсчета количества правильных ответов
        correct_answers = 0

        # Список всех композиторов
        composers = ['Mozart', 'Bach', 'Vivaldi', 'Grieg', 'Liszt',
                     'Schubert', 'Beethoven', 'Salieri', 'Tchaikovsky',
                     'Wagner']

        # Случайно выбираем 5 композиторов из списка для викторины
        result = random.sample(composers, 5)

        # Задаем участнику викторины вопросы, и проверяем ответы
        if 'Mozart' in result:
            mozart_attempt = input('введите дату рождения Моцарта\n')
            correct_answers += check_answer(mozart_attempt, mozart_birthday_year)
        if 'Bach' in result:
            bach_attempt = input('введите дату рождения Баха\n')
            correct_answers += check_answer(bach_attempt, bach_birthday_year)
        if 'Vivaldi' in result:
            vivaldi_attempt = input('введите дату рождения Вивальди\n')
            correct_answers += check_answer(vivaldi_attempt, vivaldi_birthday_year)
        if 'Grieg' in result:
            grieg_attempt = input('введите дату рождения Грига\n')
            correct_answers += check_answer(grieg_attempt, grieg_birthday_year)
        if 'Liszt' in result:
            liszt_attempt = input('введите дату рождения Листа\n')
            correct_answers += check_answer(liszt_attempt, liszt_birthday_year)
        if 'Schubert' in result:
            schubert_attempt = input('введите дату рождения Шуберта\n')
            correct_answers += check_answer(schubert_attempt, schubert_birthday_year)
        if 'Beethoven' in result:
            beethoven_attempt = input('введите дату рождения Бетховена\n')
            correct_answers += check_answer(beethoven_attempt, beethoven_birthday_year)
        if 'Salieri' in result:
            salieri_attempt = input('введите дату рождения Сальери\n')
            correct_answers += check_answer(salieri_attempt, salieri_birthday_year)
        if 'Tchaikovsky' in result:
            tchaikovsky_attempt = input('введите дату рождения Чайковского\n')
            correct_answers += check_answer(tchaikovsky_attempt, tchaikovsky_birthday_year)
        if 'Wagner' in result:
            wagner_attempt = input('введите дату рождения Вагнера\n')
            correct_answers += check_answer(wagner_attempt, wagner_birthday_year)

        # Переменная для неправильных ответов
        incorrect_answers = 5 - correct_answers

        # Выводим в терминал количество правильных ответов
        print('Количество правильных ответов', correct_answers)

        # Выводим в терминал количество неправильных ответов
        print('Количество неправильных ответов', incorrect_answers)

        # Выводим в терминал процент правильных ответов
        print('Процент правильных ответов', correct_answers * 100 / 5)

        # Выводим в терминал процент неправильных ответов
        print('Процент неправильных ответов', incorrect_answers * 100 / 5)

        play_again = input('\nХотите сыграть еще раз?\n')
        if play_again == 'да':
            pass
        else:
            break
