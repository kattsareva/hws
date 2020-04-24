# benefit - прибыль
# costs - издержки
# workers - работники

benefit = float(input('Какая прибыль: '))
costs = float(input('Какие издержки: '))

if benefit > costs:
    print(f'Прибыль есть. Выручка: {benefit / costs:.2f}')
    workers = int(input('Сколько работников: '))
    print(f'Прибыль на одного работника: {benefit / workers:.2f}')
elif benefit == costs:
    print('Прибыли нет.')
else:
    print('Убытоное производство')