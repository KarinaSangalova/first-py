try:
    a = int(input('Введите длину первого катета прямоугльного треугольника: '))
    b = int(input('Введите длину второго катета прямоугольного треугольника: '))
except:
    print('Это не число')
    a = int(input('Введите длину первого катета прямоугльного треугольника: '))
    b = int(input('Введите длину второго катета прямоугольного треугольника: '))
s = 0.5*a*b
c2 = a**2+b**2
c = int(c2**0.5)
p = a+b+c
print('Площадь прямоугольного тругольника равна: ', s)
print('Периметр прямоугольного треугольника равен: ', p)