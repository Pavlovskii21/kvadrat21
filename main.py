import math
 a*x^2 +bx + c = 0

a = int(input())
b = int(input())
c = int(input())

D = b ** 2 - 4*a*c
Droot = math.sqrt(D)
# x = (-b -+ sqrt(D))/(2a)
#если D > 0
#x = -b/2a
#если D == 0
#нет корней
#если D < 0
if D > 0
 x=(-b-+sqrt(D))/(2a)
elif D == 0
 x = -b/2a
else D < 0
 x=0