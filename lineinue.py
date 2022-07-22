

# a * x + b = 0
a = float(input('Ввведите коэффициент а:'))
b = float(input('Ввведите коэффициент b:'))

if a != 0:
    x = -b / a
    print(x)
elif a == 0 and b == 0:
    print("любое число ")
else:
    print('Нет корней')
