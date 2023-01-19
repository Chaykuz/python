# start_number = 10
# end_number = 100
# for dividers in range(start_number, end_number):
#   if int(3 * (dividers // start_number) * (dividers % start_number)) == int(dividers):
#     print(dividers)

all_card = int(input('Введите количество карточек: '))
sum_all_card = all_card
sum_know_card = 0
for card in range(1, all_card):
    sum_all_card += card
    sum_know_card += int(input('Введите номер оставшейся карточки: '))
print('Номер пропавшей карточки:', sum_all_card - sum_know_card)