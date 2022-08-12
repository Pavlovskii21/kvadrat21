
import math
import linear

def FindDiscr(a, b, c):
    D = b ** 2 - 4 * a * c
    return D

def kvadratnoe(a, b, c):
    if a == 0:
        linear.linear(b, c)
    else:
        D = FindDiscr(a, b, c)
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            return (x1, x2)
        elif D == 0:
            x1 = -b / (2 * a)
            return (x1, x1)
        else:
            return (False, False)
