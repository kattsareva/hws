def rewrite_f():
    num = {'One': 'Один', "Two": 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    new_text = []

    try:
        with open('text2', 'r+', encoding="utf-8") as file:
            with open('new_file', 'r+', encoding="utf-8") as new_file:
                r = file.readlines()
                for i in r:
                    i = i.split(' ', 1)
                    new_text.append(num[i[0]] + ' ' + i[1])
                new_file.writelines(new_text)

    except FileNotFoundError:
        return 'Файл не найден.'

rewrite_f()