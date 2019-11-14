import requests
import json
from xlwt import *

# I'll go for current weather at Mace Head
url = "https://prodapi.metweb.ie/observations/mace-head/today"

response = requests.get(url)
data = response.json()

# check
for i in data:
    print(i["windSpeed"])

# Write to excel file
w = Workbook()
ws = w.add_sheet('weather')

# At row 0 place column headings text
row = 0
ws.write(row, 0, "date")
ws.write(row, 1, "dayName")
ws.write(row, 2, "reportTime")
ws.write(row, 3, "temperature")
ws.write(row, 4, "weatherDescription")
ws.write(row, 5, "windSpeed")

# Move to next row
row += 1

# Now write the data
for obs in data:
    ws.write(row, 0, obs["date"])
    ws.write(row, 1, obs["dayName"])
    ws.write(row, 2, obs["reportTime"])
    ws.write(row, 3, obs["temperature"])
    ws.write(row, 4, obs["weatherDescription"])
    ws.write(row, 5, obs["windSpeed"])
    row += 1
w.save('MaceHeadWeather.xls')


# # save this to a file
# filename = 'MaceHeadWeather.json'
# # Writing JSON data
# f =  open(filename, 'w')
# json.dump(data, f, indent=4)