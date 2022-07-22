import math
# a*x^2 +bx + c = 0
a = float(input('Ввведите коэффициент а:'))
b = float(input('Ввведите коэффициент b:'))
c = float(input('Ввведите коэффициент c:'))

D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(x1, x2)
elif D == 0:
    x = -b / (2 * a)
    print(x)
else:
    print('Нет корней')
