min = int(input('Введите число минут: '))

hour = min // 60 
rest_min = min % 60
print('Часов: ', hour)
print('Оставшиейся минуты', rest_min)