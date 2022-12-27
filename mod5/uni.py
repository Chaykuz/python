

points = int(input('Сколько баллов набрал? '))
medal = int(input('Есть медаль? '))
pass_score = 280

if points > pass_score and medal == 1: 
    print('Поздравляем! Ты поступил!')
else: 
    print('К сожалению, ты не прошёл в наш университет.')
