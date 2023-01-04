# connect to an api
import json

import requests

# get the data from the api
response = requests.get("https://api.hypixel.net/skyblock/bazaar")
# response in an object

# get the data from the response
data = response.json()

# print(data)

# save data to file
with open("bazaar.json", "w") as file:
    json.dump(data, file)
    print("Data saved to file")

print(data)

