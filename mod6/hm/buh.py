while True:
    num = int(input('Введите число: '))
    num_count = 0
    if num == 0:
        num_count = 1
    else:
        while num != 0:
            num_count += 1 
            num //= 10
    print('Количество знаков в числе:', num_count)