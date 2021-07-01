# Создать универсальный декоратор, который меняет порядок аргументов в
# функции на противоположный

def my_dec(fun):
    def wraper(*args):
        new_arg = args[::-1]
        return fun(new_arg)

    return wraper


@my_dec
def my_print(*args):
    for i, arg in enumerate(*args):
        print(i, arg)
