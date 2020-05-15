def calc():
    hours = float(input('Количество отработанных часов: '))
    work = float(input('Оплата работы в час: '))
    benefit = float(input('Размер премии: '))
    pay = hours * work
    return pay + benefit

print(f'Размер зарплаты: {calc()}')