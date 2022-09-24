road = 115
speed = int(input('Введите скорость(км/ч): '))
time = int(input('Время поездки: '))

pass_road = speed * time
print('Длина пройденного расстояние будет равна: ', pass_road)
loops = pass_road // road
km = (speed * time) % road
print('Вася прошел: ', loops, 'круг(ов) и', km, 'километров')
