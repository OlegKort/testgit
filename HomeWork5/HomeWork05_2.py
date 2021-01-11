print("Ноль в качестве знака операции завершит работу программы")
while True:
    z = input("Знак (+,-,*,/): ")
    if z == '0': break
    if z in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if z == '+':
            print("%.2f" % (x + y))
        elif z == '-':
            print("%.2f" % (x - y))
        elif z == '*':
            print("%.2f" % (x * y))
        elif z == '/':
            if y != 0:
                print("%.2f" % (x / y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")
