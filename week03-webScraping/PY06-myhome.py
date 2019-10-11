## Elizabeth Daly
## Data Representation Lab 3 PY06-myhome.py

# Import requests package
import requests
# Import Beautiful Soup package
from bs4 import BeautifulSoup
# Import csv package.
import csv

# URL of page to retrieve
# Page 1 of Residential houses for sale in Mayo
page = requests.get("https://www.myhome.ie/residential/mayo/house-for-sale?page=1")

soup = BeautifulSoup(page.content, 'html.parser')

# # print pretty version.
# print("----")
# print(soup.prettify())

# set up file to store results.
home_file = open('week03MyHome.csv', mode='w')
home_writer = csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

listings = soup.findAll("div", class_="PropertyListingCard") 

for listing in listings:
    entryList = [] # Empty list each property
    # print("----")
    price = listing.find(class_="PropertyListingCard__Price").text
    entryList.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text
    entryList.append(address)
    # print(entry)
    # write list to row in file.
    home_writer.writerow(entryList)

home_file.close()

""" ############################################################
# Find first <div> with class='PropertyListingCard'
listings = soup.find("div", class_="PropertyListingCard") 
print(listings)

# Find price part 15
price = listings.find(class_="PropertyListingCard__Price").text
print(price)

# and address part 16
address = listings.find(class_="PropertyListingCard__Address").text
print(address)
 """