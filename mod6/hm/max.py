print('Начался 8-часовой рабочий день')
Total_Task = 0
wife_flag = False
hour_count = 1
while hour_count != 9:
    print(hour_count, '-й час')
    task = int(input('Сколько задач решит Максим? '))
    Total_Task += task
    wife = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
    if wife == 1:
        wife_flag = True
    hour_count += 1
print('Рабочий день закончился. Всего выполнено задач: ', Total_Task)

if wife_flag:
    print('Нужно зайти в магазин.')