player = int(input('Кубик Кости: '))
owner = int(input('Кубик владельца: '))

if player >= owner: 
    jackpot = player - owner
    print('Костя платит')
else: 
    jackpot = player + owner
    print('Владелец платит')
    

print('Сумма', jackpot)
print('Игра окончена')