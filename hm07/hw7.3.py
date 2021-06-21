# Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε —
# вещественные, ε > 0), находящую приближенное значение функции sin( x ):
# sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
# В сумме учитывать все слагаемые, модуль которых больше ε . С помощью
# Sin1 найти приближенное значение синуса для данного x при шести данных
# ε

from math import *

# --- variables
n = 20
x = 3
eps = [0.001, 0.02, 0.1, 0.2, 0.3, 0.5]


# -------------
def mc_loren_cos(x, n, eps):
    res = 0
    while (n):
        elem = (pow(-1, n) * pow(x, 2 * n)) / factorial(2 * n)
        if abs(elem) > eps:
            res += elem
        n -= 1
    return res


def mc_loren_sin(x, n, eps):
    res = 0
    while (n):
        elem = (pow(-1, n) * pow(x, 2 * n + 1)) / factorial(2 * n + 1)
        if abs(elem) > eps:
            res += elem
        n -= 1
    return res


for i in range(0, 6):
    print("Sin(x) when n = " + str(n) + " , x = " + str(x) + " , eps =" + str(eps[i]))
    print(mc_loren_sin(x, n, eps[i]))

for i in range(0, 6):
    print("Cos(x) when n = " + str(n) + " , x = " + str(x) + " , eps =" + str(eps[i]))
    print(mc_loren_cos(x, n, eps[i]))
