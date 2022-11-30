from bank_functions import donate, buy, buy_dict


def bank_program():
    # Сумма на счету
    balance = 0
    # Список покупок
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
            purchase = input('введите название покупки\n')
            balance, purchase_dict = buy(balance, price, purchase, purchase_dict)
        elif choice == '3':
            buy_dict(purchase_dict)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    bank_program()
