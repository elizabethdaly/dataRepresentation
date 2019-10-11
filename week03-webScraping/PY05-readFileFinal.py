## Elizabeth Daly
## Data Representation Lab 3 PY05-readFileFinal.py

# Import requests package.
import requests
# Import Beautiful Soup package.
from bs4 import BeautifulSoup
# Import csv package.
import csv

# Open the file from week 2 lab
with open("../week02/carviewer_wk2.html") as f:
    soup = BeautifulSoup(f, 'html.parser')

# Open/create a file in write mode.
new_file = open('week02data.csv', mode='w')

# set up pars.
new_writer = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# For each row of table in html file, store text in columns in a list.
rows = soup.findAll("tr")
for row in rows:

    dataList = []  # Start with empty list for each row.
    cols = row.findAll("td")
    for col in cols:
        dataList.append(col.text)
    new_writer.writerow(dataList[0:4])   # Write this row to new_file omitting update/delete text

new_file.close()

# If don't want update/delete text output? 
# Don't write full dataList to file, just first 4 elements