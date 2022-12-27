total_mouths = int(input('Сколько месяцев будем копить? '))
summ = 0
for month in range(total_mouths): 
    print('Месяц ', month)
    money = int(input('Сколько рублей откладываем? '))
    summ += money
print('За', total_mouths, 'месяцев ты накопишь', summ, ' рублей.')