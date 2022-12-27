x = int(input('Введите 1 число: '))
y = int(input('Введите 2 число: '))
z = int(input('Введите 3 число: '))

if x == y and x == z and y == z: 
    print('Все числа совпадают')
elif x == y or x == z or y == z:
    print('Совпадают 2 числа')
else:
    print('Числа не совпадают')
