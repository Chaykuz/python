money = int(input('Введите количество денег: '))

if money >= 60: 
    print('На сыр денег хватило')
    money -= 60
    if money >= 20:
        print('И на мороженное тоже!')
        money -= 20 
    else:
        print('На мороженное не хватает.')
else:
    print('Денег маловато')
print('Баланс: ', money)
