number = int(input('Введите номер билета (6цифр): '))
luck_start = (number // 100000) + (number // 10000 % 10) + (number // 1000 % 10)
luck_end = (number % 1000 // 100) + (number % 100 // 10) + (number % 10)
while luck_start != luck_end:
    print('Повезет  в следующий раз, это не счастливый билет :(')
    number = int(input('Введите номер билета (6цифр): '))
    luck_start = (number // 100000) + (number // 10000 % 10) + (number // 1000 % 10)
    luck_end = (number % 1000 // 100) + (number % 100 // 10) + (number % 10)
print('Ура! Счастливый билет!')


