from random import random


son = int(input('Загадай число: '))
father = 7

if son == father: 
    print('Угадал!')
else: 
    print('Не угадал!')
print('Конец игры')

son = int(input('Загадай число: '))


if son != father: 
    print('Не угадал!')
else:
    print('Угадал!')
print('Конец игры')
