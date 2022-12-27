# count = int(input('Введите время: '))
# while count >= 0:
#     print(count)
#     if count == 0:
#         print('Время вышло!')
#     count -= 1

# while True: 
#     active = int(input('Продолжаем работать? 1/0: '))
#     if active == 0:
#         print('Приложение закрывается...')
#         break
# print('Работа завершена')

unlock = "0550"
while True:
    print('Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!')
    pasw = input('Введите код: ')
    if pasw == unlock:
        print('Код верный, завершаю работу...')
        break
