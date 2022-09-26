mileage = int(input('Введите пробег: '))
today = int(input('Введите сегодняшнее число: '))

num1 = mileage // 100
num2 = (mileage // 10) % 10
num3 = mileage % 10 

s_number = num1 + num2 + num3

if s_number > today: 
    mileage = 0
    print('Сброс')
else: 
    print('Сегодня не сломался.')
print('Пробег: ', mileage)