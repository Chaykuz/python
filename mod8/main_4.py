# микр 

# seconds = int(input('Введите кол-во секунд: '))
# for sec in range(seconds, 0, -1):
#     print('Микроволновка греет: ', sec)
# print('Дзынь!')

# армия 

# totalSoldier = int(input('Кол-во солдат в шеренге: '))
# total_rules = int(input('Сколько правил в уставе? '))
# push_ups = 0
# for soldier in range(totalSoldier, 0, -4):
#     soldier_rules = int(input('Солдат, назови кол-во правил в уставе: '))
#     if total_rules != soldier_rules:
#         print('Неправильно!', 10 * soldier, 'отжиманий!')
#         push_ups += 10 * soldier
# print('Общее кол-во отжиманий: ', push_ups)

# прятки 

# seconds = int(input('Сколько секунд считаем? '))
# for n in range(seconds, 0, -1):
#     print(n)
# print('Я иду искать!')

# Армия - 2 

# totalSoldier = int(input('Кол-во солдат в шеренге: '))
# total_rules = int(input('Сколько правил в уставе? '))
# push_ups = 0
# for soldier in range(totalSoldier - 4, 0, -4):
#     soldier_rules = int(input('Солдат, назови кол-во правил в уставе: '))
#     if total_rules != soldier_rules:
#         print('Неправильно! ', 10 * soldier,'отжиманий!' )
#         push_ups += 10 * soldier
# print('Общее кол-во отжиманий:')

# прятки - 2

n = int(input('Сколько секунд считаем? '))
even_n = n - n % 2
for i in range(even_n, 0, -2):
    print(i)
print('Я иду искать!')