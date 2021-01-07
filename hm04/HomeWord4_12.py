a = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
keys = list(a.keys())
b = 0

while b < len(keys):
    key = keys[b]
    a[key + str(len(key))] = a.get(keys[b])
    a.pop(key)
    b += 1

print(a)

# .Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
# Чтобы получить список ключей - использовать метод .keys()
# (подсказка: создается новый ключ с цифрой в конце, старый удаляется)
dictionary = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

for key in list(dictionary):
    dictionary[key + str(len(key))] = dictionary.get(key)
    dictionary.pop(key)
print(dictionary)
