balance = int(input('Введите баланс лицевого счета: '))

if balance >= 75000:
    balance -= 75000
    print('Курс успешно приобретён.')
    if balance < 5000:
        balance += 1000
        print('Сделана скидка')
else: 
    print('Не хватает денег на счёте.')
print('Баланс: ', balance)
print('Хорошего дня')

