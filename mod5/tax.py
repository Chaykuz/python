profits = int(input('Введите ваш доход: '))
tax = 0

# if profits < 10000:
#     tax = profits * 13 / 100
#     print('Ставка налога 13%: ', tax)
# elif profits < 50000:
#     tax = profits * 20 / 100
#     print('Ставка налога 20%: ', tax)
# elif profits >= 50000:
#     tax = profits * 30 / 100
#     print('Ставка налога 30%: ', tax)
# elif profits < 0:
#     print('Доход не может быть отрицалтельным: ')

if profits < 0:
    print('Доход не может быть отрицалтельным')
elif profits < 10000:
    tax = profits * 13 / 100
    print('Ставка налога 13%: ', tax)
elif profits < 50000:
    tax = profits * 20 / 100
    print('Ставка налога 20%: ', tax)
else: 
    tax = profits * 30 / 100
    print('Ставка налога 30%: ', tax)

