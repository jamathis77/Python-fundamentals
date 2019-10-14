# To create a virtual environment: <python> -m venv <a-name-here>
# To activate virtual environment: 
#       Windows:  <a-name-here>/Scripts/activate
#     Mac(linx): source <a-name-here>/bin/activate
# To verify: Terminal should have the virt-env on the left
# 

import requests
from pprint import pprint

api_url = "https://rickandmortyapi.com/api/"

character_response = requests.get(api_url + "character")
try:
    data = character_response.json()
except Exception:
    data = None

choices = data['info']['count']

choice = input(f"Pick a number between 1 and { choices } > ")

chosen = requests.get(api_url + "character/" + choice)

print(chosen.headers)

chosen_one = chosen.json()

print(chosen_one["name"])




# response = requests.get("https://api.spacexdata.com/v3/rockets")
# data = response.json()

# pprint(data)

# for entry in data:
#     print(entry['rocket_name'], "\n")