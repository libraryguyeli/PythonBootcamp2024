import random
import csv

print(random.randint(1,1000))

def add(a, b):
    return a + b

print("ADD:", add(1, 2))

with open("customers-100.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        if int(row['Index']) % 5 == 0:
            print(f"{row['First Name']} {row['Last Name']}, {row['Company']}")

with open("test.txt", "a") as txt_file:
    for i in range(1,11):
        txt_file.write("#" * i + "\n")
    for i in range(11,1,-1):
        txt_file.write("#" * i + "\n")