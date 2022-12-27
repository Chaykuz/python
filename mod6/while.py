# number = int(input('Введите число: '))
# summ = 0
# while number != 0:
#     summ += number
#     number = int(input('Введите число: '))
# print(summ)

# password = 235

# user = int(input('Введите пароль: '))

# while user != password:
#     print('Пароль неверный.')
#     user = int(input('Введите пароль снова: '))
# print('Пароль принят!')
# print('Добро пожаловать.')


pig_salary = int(input('Сколько отложить денег? '))
bank = 0
while bank < 500000:
    bank = bank + pig_salary
    pig_salary = int(input('Пока не хватает, нужно отложить еще: '))
print('Денег хватает, едем за машиной!')
     