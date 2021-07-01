# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
# это порядковый номер строки в списке. Использовать генератор списков.


text = ['zero', 'one', 'two', 'three', 'four', 'five']

for number, strings in enumerate(text):
    print(number, strings)


