

number = int(input('Введите число: '))

if number < 0: 
    normilze = max(-number, number)
    normalize = (number * number) ** .5
    print('Число через max: ', normilze)
    print('Число через квадратный корень', normalize)