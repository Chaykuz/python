task = int(input('Какой вариант задачи 1 или 2? '))
time = int(input('Время похода в отделение: '))

if task == 1:
    if (time >= 10 and time <= 12) or (time >= 18 and time <= 20): 
        print('Посылку получить нельзя идет разгрузка посылок')
    elif time >= 14 and time <= 15:
        print('Посылку получить нельзя. Отделение на обеде.')
    elif time < 8 or  time > 22:
        print('Посылку получить нельзя. Отделение не работает!')
    else:
        print('Можно получить посылку')
else:
    if (time >= 10 and time <= 12) or (time >= 18 and time <= 20): 
        print('Можно получить посылку')
    elif time >= 14 and time <= 15:
        print('Можно получить посылку.')
    elif time < 8 or  time > 22:
        print('Можно получить посылку!')
    else:
        print('Посылку получить нельзя')
