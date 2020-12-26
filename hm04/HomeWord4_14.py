list_fib = [1, 1]

while len(list_fib) <= 15:
    list_fib.append(list_fib[len(list_fib) - 1] + list_fib[len(list_fib) - 2])

print(list_fib)