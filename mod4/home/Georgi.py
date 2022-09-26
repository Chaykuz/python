timely = int(input('Введите отработанные часы: '))
credit = int(input('Введите остаток по кредиту: '))
eat = int(input('Введите трату на еду: '))

salary = ((200 * timely) / 2 ** 3) + timely

exps = credit + eat

if salary > exps: 
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придётся работать!')