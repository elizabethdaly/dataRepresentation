# Lab06_01_part5.py

# Import required packages.
import requests # to send http requests
import json     # to handle json
from xlwt import *  # Excel

# All users that are following AB on GitHub
url = "https://api.github.com/users/andrewbeattycourseware/followers"

# Do the GET
response = requests.get(url)
data = response.json()

# a. Output to console
# print(data)

# Output followers individually
for user in data: #["followers"]:
    print(user)

# b. Output to a file
filename = 'githubusers.json'
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)

# Write to an excel workbook
# Only do first four properties for each user: login, id
w = Workbook()  # create new workbook
ws = w.add_sheet('users')    # make a new sheet

# At row 0 place column headings text
row = 0
ws.write(row, 0, "login")
ws.write(row, 1, "id")
ws.write(row, 2, "node_id")
ws.write(row, 3, "avatar_url")

# Move to next row
row += 1

for user in data: #["followers"]:
    ws.write(row, 0, user["login"])
    ws.write(row, 1, user["id"])
    ws.write(row, 2, user["node_id"])
    ws.write(row, 3, user["avatar_url"])
    row += 1
w.save('followers.xls')
