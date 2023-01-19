# гречка

# food = 100
# mounth_cound = 1
# for food in range(food, -1, -4):
#     print('Месяц', mounth_cound)
#     mounth_cound += 1
#     print('Осталось гречки =', food)
#     if food != 0:
#         print('Еще осталось гречка!')
#     else:
#         print('Гречка кончилась!')

# Долги

# debet = int(input('Введите кол-во должников: '))
# debet_sum = 0
# for i in range(0, debet, 5):
#     print('Должник с номером ', i)
#     debet_debt = int(input('Сколько должны? '))
#     debet_sum += debet_debt
# print('Общая сумма долга: ', debet_sum)

# Микроволновка 

# reverse_timer = int(input('Введите кол-во секунд: '))
# ready_flag = 1
# timer_count = 0
# for sec in range(reverse_timer, 0, -1):
#     print('Микроволновка греет: ', sec)
#     timer_count += 1
#     ready = int(input('Вы хотите забрать еду? '))
#     if ready == ready_flag:
#         print('Ваша еда готова, можете забрать')
#         break;
#     elif sec == 1:
#         print('Ваша еда готова, осторожно горячo!')
# print('Микроволновка грела: ', timer_count, 'секунды')

# Среднее на отрезке

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# c = int(input('Введите третье число: '))
# number_sum = 0
# for number in range(a,b + 1, 1):
#     number_sum += number
# print('Среднее арифмитическое всех числе из отрезка', a,'и ', b,' кратное числу 3 = ', number_sum // c)

# Функция 2 
# begin_number = int(input('Введите начало отрезка: '))
# end_number = int(input('Введите конец отрезка: '))
# step = int(input('Введите шаг: '))
# for i in range(end_number, begin_number - 1, step):
#     print('В точке ', i,' функция равна ', i**3 + 2*i**2 - 4*i + 1)


# Письмо 

# letter = int(input('Введите размер письма: '))
# count_fold = 0
# enve = 12
# for z in range(letter):
#     if letter <= enve:
#         break
#     letter /= 2
#     count_fold += 1
# print('Письмо сложили ', count_fold, 'раз, теперь оно войдет в конверт 12x12')

# Стипендия 

# grant = int(input('Введите размер стипендии: '))
# expens = int(input('Введите расходы на проживание: '))
# parents_money = 0
# firts_exp = expens - grant
# for time in range(1, 10, 1):
#     expens += expens * 3 / 100
#     parents_money += expens - grant
# print('Необходимо взять у родителей ', parents_money + firts_exp)
    

# Сумма ряда

# n = int(input('Введите число n: '))

# for number in range(1, n, 4):
#     s = 1 - 1 / number + 1 / number - 1 / number + ((-1) ** number) * 1 / 2 ** number
# print('Сумма ряда = ', s)

# # Выражение 


# number = int(input('Введите число x для вычисления выражения: '))
# numerator = 1
# denonumerator = 1
# result = 1
# for N in range (1, 6 + 1):
#   numerator *= (number - (2 ** N - 1))
#   denonumerator *= (number - (2 ** N))
#   result = numerator / denonumerator
# print('Результат равен: ', result)

# кино 

# boys = int(input('Введите кол-во малчиков: '))
# girls = int(input('Введите кол-во девочек: '))
# result = ''
# if (boys // 2 > girls) or (girls // 2 > boys):
#     print('Нет решения.')
# elif boys >= girls:
#     k = boys - girls
#     for i in range(k):
#         result += 'BGB'
#     for j in range(girls - k):
#         result += 'BG'
# else:
#     k = girls - boys
#     for i in range(k):
#         result += 'GBG'
#     for j in range(boys - k):
#         result += 'GB'
# print('Рассадка ', result)
