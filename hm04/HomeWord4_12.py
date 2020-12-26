a = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
keys = list(a.keys())
b = 0

while b < len(keys):
    key = keys[b]
    a[key + str(len(key))] = a.get(keys[b])
    a.pop(key)
    b += 1

print(a)
