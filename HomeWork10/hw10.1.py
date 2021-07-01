# Создать csv файл с данными следующей структуры: Имя, Фамилия,
# Возраст. Создать отчетный файл с информацией по количеству людей
# входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18,
# 19-25, 26-40, 40+.

import csv

# from cw.cw10.task_10_03 import *

FILENAME = "users.csv"

users = [
    {"name": "Anna Semenovich", "age": 32},
    {"name": "Anfisa Pompushka", "age": 24},
    {"name": "Ivan Urgart", "age": 41},
    {"name": "Yuriy Stayanov", "age": 63},
    {"name": "Margo Robby", "age": 20},
    {"name": "Petya Smiroff", "age": 14},
    {"name": "Yuriy Hoy", "age": 5}
]

kids = []
teenager = []
junior = []
adults = []
aged = []
for i in users:
    if i["age"] > 40:
        aged.append(i)
    if i["age"] in range(26, 40):
        adults.append(i)
    if i["age"] in range(19, 25):
        junior.append(i)
    if i["age"] in range(13, 18):
        teenager.append(i)
    elif i["age"] in range(1, 12):
        kids.append(i)

summ = [kids, teenager, junior, adults, aged]


with open(FILENAME, "w", newline="") as file:
    columns = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()

    for new_users in summ:
        writer.writerows(new_users)

    with open(FILENAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["name"], "-", row["age"])
