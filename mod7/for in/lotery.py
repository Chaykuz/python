winners = 0 
for  ticket in 345, 19, 87, 1020, 555:
    if ticket % 5 == 0 and 99 < ticket < 1000:
        print(ticket, '- Счастливый билет')
        winners += 1
print ('Кол-во победителей', winners)