first_quart = int(input('Введите доход за 1 квартал: '))
second_quart = int(input('Введите доход за 2 квартал: '))
three_quart = int(input('Введите доход за 3 квартал: '))
four_quart = int(input('Введите доход за 4 квартал: '))

begin_year = first_quart + second_quart
end_year = three_quart + four_quart
fin_dinamics = begin_year / end_year

print(fin_dinamics)