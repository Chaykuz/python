wake_up = int(input('Во сколько проснулся: '))
awake_hours = 0
calories_sum = 0
for hour in range(wake_up, 23):
    print('Сейчас ', hour, 'часов')
    calories = int(input('Сколько съел за час? '))
    calories_sum += calories
    if calories_sum > 2000:
        print('Хорошо поел, можно и поспать.')
        break
    awake_hours += 1
print('Съедено калорий за день', calories_sum)
print('Часов не спал: ', awake_hours)



# v2 

