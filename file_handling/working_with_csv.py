import csv
"""     
with open('california_housing_test.csv', mode = 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
 """
import csv

data = [["Name", "Age", "Country"],
        ['Alice', 28, 'USA'],
        ['Bob', 32, 'Australia']
        ]

with open('output.csv', mode = "w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
