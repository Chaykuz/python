totalCard = int(input('Введите кол-во '))
totalSum = 0
remaining_sum = 0
for card in range(1, totalCard + 1):
    totalSum += card
for card in range(totalCard-1):
    remaining_card = int(input('Номер оставшейся карты: '))
    remaining_sum += remaining_card
summ = totalSum - remaining_sum
print('Номер потерявшейся карты: ', summ)