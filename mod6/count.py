# text = 'Я — программист!'
# text__count = 0
# count = int(input('Сколько раз вывести строку? '))

# while text__count < count:
#     print(text)
#     text__count += 1

n = int(input("Сколько раз ходили на рыбалку? "))
fishing_count = 0
fish_weight = 0

while fishing_count < n:
    fish_weight += int(input("Сколько поймали? "))
    fishing_count += 1

print("Суммарный вес:", fish_weight)