father = 7
son = int(input('Введите число: '))
trying = 1

while father != son:
    print('Число меньше, чем нужно. Попробуйте ещё раз!')
    son = int(input('Введите число: '))
    trying += 1
print('Вы угадали! Число попыток: ', trying)

