days = int(input('Введите день: '))

even = days % 2 

if even != 1: 
    print('Сегодня нужно использовать зубную нить')
else: 
    print('Сегодня без зубной нити')
