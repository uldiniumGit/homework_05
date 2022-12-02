from bank_functions import donate, buy, buy_dict
import os.path
import json


def bank_program():
    # Сумма на счету
    if os.path.exists(os.getcwd() + '/balance.txt'):
        with open("balance.txt") as file:
            balance = int(file.read())
    else:
        balance = 0

    # Список покупок
    if os.path.exists(os.getcwd() + '/mydict.txt'):
        with open('mydict.txt') as purchases:
            purchase_dict = json.load(purchases)
    else:
        purchase_dict = {}

    while True:
        print('')
        print(f'у вас на счету сейчас {balance} рублей')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню\n')

        if choice == '1':
            deposit = int(input('введите сумму пополнения\n'))
            balance = donate(balance, deposit)

        elif choice == '2':
            price = int(input('введите сумму покупки\n'))
            if price > balance:
                print('у вас недостаточно средств')
            else:
                purchase = input('введите название покупки\n')
                balance, purchase_dict = buy(balance, price, purchase, purchase_dict)

        elif choice == '3':
            buy_dict(purchase_dict)

        elif choice == '4':
            balance_file = open("balance.txt", "w")
            balance_file.write(str(balance))
            balance_file.close()

            file = open("mydict.txt", "w")
            file.write(json.dumps(purchase_dict))
            file.close()
            break
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    bank_program()
