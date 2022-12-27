begin_number = int(input('Введите начальное число: '))
end_number = int(input('Введите конечнно число: '))
for number in range(begin_number, end_number + 1):
    print(number ** 2)
