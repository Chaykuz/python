total_salary = 0

for month in range(12):
    print('Месяц', month + 1)
    salary = int(input('Зарплата за месяц? '))
    total_salary += salary

medium_salary = total_salary / 12
print('Средняя зарплата за год = ', medium_salary)
