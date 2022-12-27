dep = int(input('Сколько хотите положить денег на вклад? '))
perc = int(input('Процентная ставка: '))
summ = int(input('Сколько хотите заработать? '))

year = 0

while dep < summ:
    dep += perc / 100 * dep
    dep //= 1
    year += 1

print('Вы заработаете эту сумму через:', year, 'года/лет!')