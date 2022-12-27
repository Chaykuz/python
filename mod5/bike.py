year = int(input('Введите год выпуска велосипеда: '))
speed = int(input('Введите количество скоростей: '))

if year < 2018 or speed < 24:
    print('Не подходит')
else:
    print('Подходит!')