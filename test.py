import random
import csv

print(random.randint(1,1000))

def add(a, b):
    return a + b

print("ADD:", add(1, 2))

with open("customers-100.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row['Index']) % 5 == 0:
            print(f"{row['First Name']} {row['Last Name']}, {row['Company']}")