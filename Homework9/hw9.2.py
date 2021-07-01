# Создать lambda функцию, которая принимает на вход неопределенное
# количество именных аргументов и выводит словарь с ключами удвоенной
# длины. {‘abc’: 5} -> {‘abcabc’: 5}


def my_func():
    func = lambda **kwargs: {key * 2: val for key, val in kwargs.items()}
    print(func(value_1=1, value_2=2))
my_func()