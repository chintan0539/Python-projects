import csv

with open("data.csv") as file:
    reader = csv.reader(file)
    for email in reader:
        print("email to ")