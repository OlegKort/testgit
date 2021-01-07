list_fib = [1, 1]

while len(list_fib) <= 15:
    list_fib.append(list_fib[len(list_fib) - 1] + list_fib[len(list_fib) - 2])

print(list_fib)

# Составить список чисел Фибоначчи содержащий 15 элементов.
# (подсказка: числа Фибоначчи - последовательность, в которой первые два числа равны либо 1 и 1,
# а каждое последующее число равно сумме двух предыдущих чисел. Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )

list_fib = [1, 1]
n = int(input())

for i in range(2, n):
    list_fib.append(list_fib[len(list_fib) - 1] + list_fib[len(list_fib) - 2])
print(list_fib)
