num1 = int(input('Введите 1 число: '))
num2 = int(input('Введите 2 число: '))
num3 = int(input('Введите 3 число: '))

if num1 > num2 and num1 > num3:
    print('Наибольшее число: ', num1)
elif num1 < num3 and num3 > num2:
    print('Наибольшее число: ', num3)
elif num2 > num3 and num1 < num2:
    print('Наибольшее число: ', num2)
    
        