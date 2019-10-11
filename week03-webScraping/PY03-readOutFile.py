## Elizabeth Daly
## Data Representation Lab 3 PY03-readOutFile.py

# Import requests package.
import requests
# Import Beautiful Soup package.
from bs4 import BeautifulSoup

# Open the file from week 2 lab.
with open("../week02/carviewer_wk2.html") as f:
    soup = BeautifulSoup(f, 'html.parser')

# # Print first <tr> from the file part 4.
# print(soup.tr)

# # Extract and print all the <tr> part 5.
# rows = soup.findAll("tr")
# for row in rows:
#     print("-----")
#     print(row)

# # For each row, get contents of <td> part 6.
# rows = soup.findAll("tr")
# for row in rows:
#     print("--")
#     cols = row.findAll("td")
#     for col in cols:
#         print(col.text)

# For each row, store text in columns in a list.
rows = soup.findAll("tr")

for row in rows:
    dataList = []   # Start with empty list for each row.
    print("--")
    cols = row.findAll("td")
    for col in cols:
        dataList.append(col.text)
    print(dataList)
