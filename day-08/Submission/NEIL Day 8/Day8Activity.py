import csv
import json

with open('example1.csv', 'r') as file:
    reader = csv.reader(file)

    next(reader)

    for line in reader:
        print(line[0])

with open('example2.json', 'r') as file:
    data = json.load(file)

    out = json.dumps(data, indent=2)
    print(out)
