number = int(input('Введите 4-х значное число: '))
first = number // 1000
second = (number // 100) % 10
three = (number // 10) % 10
four = number % 10

print('Первое число: ', first)
print('Второе число: ', second)
print('Третье число: ', three)
print('Четвертое число: ', four)


