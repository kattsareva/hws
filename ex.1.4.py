a = int(input('Введите целое положительное число: '))

max = a % 10

while a >=1:
    if a % 10 > max:
        max = a % 10
    else:
        print('Максимальная цифра: ', max)
        break