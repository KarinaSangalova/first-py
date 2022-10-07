try:
    radius = int(input('Введите значение радиуса круга: '))
except:
    print('Это не число')
    radius = int(input('Введите значение радиуса круга: '))
s = radius**2*3.14
print('Площадь круга равна: ', s)
