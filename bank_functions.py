def donate(balance, deposit):
    '''
    Позволяет увеличить сумму на счету
    :param balance: баланс до пополнения
    :return: баланс после пополнения
    '''
    balance = balance + deposit
    return balance


def buy(balance, price, purchase, purchase_dict):
    '''
    Позволяет сделать покупку и сохранить ее название и цену
    :param balance: баланс до покупки
    :return: баланс после покупки и список покупок
    '''
    if balance >= price:
        balance = balance - price
        purchase_dict[purchase] = price
    else:
        print('у вас не хватает денег\n')
    return balance, purchase_dict


def buy_dict(purchase_dict):
    '''
    Выводит в терминал список покупок
    :param purchase_dict: список покупок
    '''
    print(purchase_dict)
    pass
