# Lab06_01_delete.py

# Import required packages.
import requests # to send http requests

# Our server from week05
url = "http://127.0.0.1:5000/cars/08%20C%201234" # Identify car to update by its reg
# %20 space

# Do the DELETE
response = requests.delete(url)
print(response.status_code)
print(response.text)