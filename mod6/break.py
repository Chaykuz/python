# temp = int(input('Введите температуру: '))
# dist = 0
# while temp > 15:
#     dist += 20
#     temp -= 2
#     if temp <= 15:
#         break
#     dist += 10
# print('Сегодня пройдено: ', dist)

# num = int(input('Введите число: '))
# summ = 0
# while num != 0:
#     last_num = num % 10
#     if last_num == 5:
#         print('Обнаружен разрыв')
#         break
#     summ += last_num
#     num //= 10
# print('Сумма', summ)

bank = int(input('Введите стартовую сумму: '))
while bank <= 10000:
    cube = int(input('Сколько выпало на кубике? '))
    if cube == 3:
        print('Вы проиграли всё!')
        bank = 0
    print('Выиграли 500 рублей!')
    bank += 500
print('Игра закончена.')
print('Итого осталось: ', bank)