import csv
with open('News.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
