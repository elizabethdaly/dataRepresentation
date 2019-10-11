## Elizabeth Daly
## Data Representation Lab 3 PY01-testRequest.py

# Import requests package
import requests
# Import Beautiful Soup package
from bs4 import BeautifulSoup

# URL of page to retrieve
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

# Print basic version
print(page)
print("----")
print(page.content)

# print pretty version
soup1 = BeautifulSoup(page.content, 'html.parser')
print("----")
print(soup1.prettify())
