# Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
# 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
# параметр целого типа. С помощью этой функции найти двойные
# факториалы пяти данных целых чисел


def factorial(a, s=1):
    if a % 2 == 0:
        for i in range(2, a + 1, 2):
            s *= i
        return s
    elif a == 0:
        return 1
    else:
        for i in range(1, a + 1, 2):
            s *= i
        return s


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print(factorial(a), factorial(b), factorial(c), factorial(d), factorial(e))


