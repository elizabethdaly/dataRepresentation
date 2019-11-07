# Lab06_01_getall.py

# Import required packages.
import requests # to send http requests
import json     # to handle json
from xlwt import *  # Excel

# Our server from week05
url = "http://127.0.0.1:5000/cars"

# Do the GET
response = requests.get(url)
data = response.json()

# Output to console
print(data)

# Output cars individually
for car in data["cars"]:
    print(car)

# Save the data to a file
filename = 'cars.json'
if filename:
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Write to an excel workbook
w = Workbook()  # create new workbook
ws = w.add_sheet('cars')    # make a new sheet

# At row 0 place column headings text
row = 0
ws.write(row, 0, "reg")
ws.write(row, 1, "make")
ws.write(row, 2, "model")
ws.write(row, 3, "price")

# Move to next row
row += 1

for car in data["cars"]:
    ws.write(row, 0, car["reg"])
    ws.write(row, 1, car["make"])
    ws.write(row, 2, car["model"])
    ws.write(row, 3, car["price"])
    row += 1
w.save('cars.xls')