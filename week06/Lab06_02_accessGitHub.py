# week06 Lab06_02_accessGitHub.py

# Import required packages.
import requests # to send http requests
import json     # to handle json

# Part 6. Get info from a private repository called
# datarepresentationstudent/aPrivateOne
# and output result to a file

# NB comment key next line before push
# On my GitHub 7/11/2019 17.28
# be4ad8ac2580705e1634fd14ebc10b828283be1-2 edit out - before use
# works in curl Part 5

apiKey = 'be4ad8ac2580705e1634fd14ebc10b828283be1-2'
url = 'https://api.github.com/repos/elizabethdaly/poems'

# File to output info to
filename = "repo.json"

# like (username, pwd)
response = requests.get(url, auth=('token', apiKey))
print(response.status_code) # should get 200

repoJSON = response.json()

# Now send info to the file
file = open(filename, "w")
json.dump(repoJSON, file, indent=4)