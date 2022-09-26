hall = int(input('Цена стула в прихожую: '))
kitchen = int(input('Цена стула на кухню: '))
bedroom = int(input('Цена стула в спальню: '))

check = hall + kitchen + bedroom

if check > 10000:
    discont = check * 10 / 100
    check -= discont
    print('Скидка применена')
print('Общая стоимость: ', check)
