# Lab06_01_update.py

# Import required packages.
import requests # to send http requests
import json     # to handle json

# Our server from week05
url = "http://127.0.0.1:5000/cars/test" # Identify car to update by reg=test

dataString = {'make': 'Ford', 'model': 'Kuga'}

# Do the PUT
response = requests.put(url, json=dataString)
print(response.status_code)
print(response.text)