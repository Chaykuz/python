num = 0
start = 1
end = 100

print('Загадайте число от 0 до 100 и я отгадаю его за 7 попыток или быстрее :)')
while num != 1:    
    binar = (start + end) // 2    
    print('Твое число равно, меньше или больше, чем число', binar, '?')
    num = int(input('Введите: 1 — равно, 2 — больше, 3 — меньше. '))
    if num == 2:        
        start = binar + 1        
    else:
        end =  binar - 1        
print('Ваше число: ', binar)