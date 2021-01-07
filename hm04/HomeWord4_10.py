a = [1, 5, 6, 8, 5, 7, 9]
length = len(a) - 1
b = []

while length >= 0:
    b.append(a[length] * -2)
    length = length - 1

b.reverse()
print(b)

# Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2
array = [1, 5, 6, 8, 5, 7, 9]
new_array = []

for element in array:
    new_array.append(element * -2)

print(new_array)