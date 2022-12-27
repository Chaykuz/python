positive = 0
negav = 0
while True:
    rate = int(input('Введите число: '))
    if rate == 0:
        break
    elif rate > 0:
        positive += 1
    else:
        negav += 1
print('Кол-во положительных отзывов: ', positive)
print('Кол-во отрицательных отзывов: ', negav)

