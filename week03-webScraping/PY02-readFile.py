## Elizabeth Daly
## Data Representation Lab 3 PY02-readFile.py

# Import requests package
import requests
# Import Beautiful Soup package
from bs4 import BeautifulSoup

## Open the file from week 2 lab
with open("../week02/carviewer_wk2.html") as f:
    soup = BeautifulSoup(f, 'html.parser')

# print pretty version
print(soup.prettify())