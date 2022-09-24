fir_num = int(input('Введите первое число: '))
sec_num = int(input('Введите второе число: '))

fir_num %= 100
sec_num %= 100

fin_num = fir_num + sec_num
print(fin_num)