a = [1, 2, 3, 4, 5, 6]
new_list = []
b = 1

while b < len(a):
    new_list.append(a[b])
    b += 1
new_list.append(a[0])
print(new_list)