a = [1, 2, 3, 4, 5, 6]
new_list = []
b = 1

while b < len(a):
    new_list.append(a[b])
    b += 1
new_list.append(a[0])
print(new_list)

# Дан список. Создать новый список, сдвинутый на 1 элемент влево Пример:12345 -> 23451
a = [1, 2, 3, 4, 5, 6]
new_list = []

for i in range(len(a)):
    if i != 0:
        new_list.append(a[i])
new_list.append(a[0])
print(new_list)
