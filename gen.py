import csv

reader = csv.reader(open('data/data.csv', 'r', encoding="utf-8"))
for i, line in enumerate(reader):
    if i == 1:
        print(line)
        break
