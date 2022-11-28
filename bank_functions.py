def donate(balance):
    '''
    Позволяет увеличить сумму на счету
    :param balance: баланс до пополнения
    :return: баланс после пополнения
    '''
    deposit = int(input('введите сумму пополнения\n'))
    balance = balance + deposit
    return balance


def buy(balance, purchase_dict):
    '''
    Позволяет сделать покупку и сохранить ее название и цену
    :param balance: баланс до покупки
    :return: баланс после покупки и список покупок
    '''
    price = int(input('введите сумму покупки\n'))
    if balance >= price:
        balance = balance - price
        purchase = input('введите название покупки\n')
        purchase_dict[purchase] = price
    else:
        print('у вас не хватает денег\n')
    return balance, purchase_dict


def buy_dict(purchase_dict):
    '''
    Выводит в терминал список покупок
    :param dict_pur: список покупок
    '''
    print(purchase_dict)
    pass