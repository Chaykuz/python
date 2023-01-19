# n = int(input('Введите число: '))
# for number in range(1,n//2+ n%2 + 1):
#     number = number * 2 - 1
#     print(number, '** 2 = ', number ** 2)


# n = int(input('Введите число: '))
# for number in range(1, n, 2):
#     print(number, '** 2 = ', number ** 2)


# Диета

# wake_up = int(input('Во сколько проснулся: '))
# water = 0
# calories_sum = 0
# for hour in range(wake_up, 23, 3):
#     water += 1
#     print('Пошли есть в', hour, 'часов')
#     calories = int(input('Сколько съел? '))
#     calories_sum += calories
# print('Выпито литров воды: ', water)
# print('Съедено калорий за день: ', calories_sum)

# Театр 

seat = int(input('Введите число '))
seat_sum = 0
for number in range(1, seat + 1, 5):
    print('Номер стула: ', number)
    seat_sum += number
print('Сумма: ', seat_sum)
    