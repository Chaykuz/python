number = int(input('Введите 4-х значное число: '))
first = number // 1000
second = (number // 100) % 10
three = (number // 10) % 10
four = number % 10

print('Первое число: ', four)
print('Второе число: ', three)
print('Третье число: ', second)
print('Четвертое число: ', first)


