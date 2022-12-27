start_numb = int(input('Введите первое число '))
end_numb = int(input('Введите второе число '))
summ = 0
for number in range(start_numb, end_numb + 1):
    summ += number
print(summ)