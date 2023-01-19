begin_number = int(input('Введите начальное чиcло: '))
end_number = int(input('Введите конечно число: '))
step = int(input('Введите шаг: '))
for number in range(begin_number, end_number + 1, step):
    print(number,'** 2 =', number ** 2)
    step += 4
    print(step)