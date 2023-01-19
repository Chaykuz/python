# n = int(input('Введите число: '))
# for number in range(1, n//2 + 1):
#     number *= 2 
#     print(number, '** 3 =',number ** 3)

totalHours = int(input('Ввелите кол-во часов: '))
cells = 1
for hour in range(1, totalHours // 3 + 1):
    cells *= 2
    print('Прошло часов: ', hour)
    print('Кол-во клеток: ', cells)
    print('Осталось часов: ', totalHours - hour * 3)
    print()
print('Наблюдения завершено!')
    