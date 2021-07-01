# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка.
from random import randint


def func_dek(fun):
    def wraper(*args):
        new_arg = [i for i in args if i % 2 == 0]
        return fun(new_arg)

    return wraper


@func_dek
def my_sum(numbers):
    return sum(numbers)
