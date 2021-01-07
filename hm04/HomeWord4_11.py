a = [2, 4, 5, 7, 8, 4]
sum = 0
length = len(a) - 1

while length >= 0:
    if a[length] % 2 == 0:
        sum += 1
    length -= 1
print(sum)

# Дан список целых чисел. Подсчитать сколько четных чисел в списке

a = [2, 4, 5, 7, 8, 4]
amount = 0
for element in a:
    if element % 2 == 0:
        amount += 1
print(amount)