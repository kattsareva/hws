def rewrite_f():
    try:
        with open('text3.txt', 'r+') as file:
            file.write(input('Напишите числа через пробел: '))
            k = map(int, file.read().split())
            print(sum(k))

    except FileNotFoundError:
        return 'Файл не нашёлся.'

rewrite_f()