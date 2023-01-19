factorial = 1

num = int(input('Введите число: '))
for i in range(2, num + 1):
  factorial *= i
print('Факториал числа', num, 'равен', factorial)