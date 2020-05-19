def workers_stat():
    workers = [['Третьяков', '19000 \n'], ['Достоевский', '14500\n'], ['Жуков', '12000\n'], ['Плисецкая', '80000\n']]
    try:
        with open('text1', 'r+', encoding="utf-8") as file:
            for i in range(len(workers)):
                file.writelines(workers[i])

            l = file.readlines()
            poor = []
            sum = 0

            for i in range(len(l)):
                salary = int((l[i].split())[1])
                if salary < 20000:
                    poor.append((l[i].split())[0])

                sum += salary

            print(f'Средний доход равен: {sum / len(workers) / 12:.2f}')
            print(f'Меньше 20 тыс. получают: {", ".join(poor)}')

    except FileNotFoundError:
        return 'Файл не был найден.'

workers_stat()