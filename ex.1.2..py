sec = int(input('Введите '))

hours = sec // 3600
minutes = (sec - hours * 60) // 3600
seconds = sec % 60

print(hours, 'часов', minutes, 'минут', seconds, 'секунд')