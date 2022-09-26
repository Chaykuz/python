russian_lang = int(input('Введите количество баллов по русскому языку: '))
mat = int(input('Введите количество баллов по математике: '))
inform = int(input('Введите количество баллов по информатике: '))
passing_score = 270

total_point = russian_lang + mat + inform

if total_point >= passing_score:
    print('Поздравляю, ты поступил на бюджет!')
else: 
    print('К сожалению, ты не прошёл на бюджет.')
    