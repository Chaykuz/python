a = int(input('Введите число а: '))
b = int(input('Введите число b: '))

summ = 0
count = 0
for sect in range(a, b + 1):
    if sect % 3 == 0:
        count += 1
        summ += sect
if count == 0:
    print('Расчет невозможен, так как нет подходящих чисел')
else:
    print(summ / count)