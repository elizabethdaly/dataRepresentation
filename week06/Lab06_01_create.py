# Lab06_01_create.py

# Import required packages.
import requests # to send http requests
import json     # to handle json

# Our server from week05
url = "http://127.0.0.1:5000/cars"

dataString = {'reg': '08 C 1234', 'make': 'Ford', 'model': 'Galaxy', 'price': 1234}

# Do the POST
response = requests.post(url, json=dataString)
print(response.status_code)