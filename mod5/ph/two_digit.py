number = int(input('Введите число: '))

if number < 0:
    number = -number

if number >= 10 and number <= 99:
    print('Двухзначное')
else:
    print('Не двузначное')