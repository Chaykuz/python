three = 0
four = 0
five = 0
student = int(input('Введите число учеников: '))
 
for z in range (1, student + 1):
  n = int(input('Введите оценку ' + str(z) + ' ученика: '))
  if n == 5:
      five += 1
  elif n == 4:
    four += 1
  else:
    three += 1
 
if five > four and five > three:
  print('Отличников сегодня больше')
if four > five and three:
  print('Хорошистов сегодня больше')
else: 
  print('Троечников сегодня больше')