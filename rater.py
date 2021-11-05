import json

file_json = open("substat_list.json")

data = json.loads(file_json.read())

print(data['Ampas']['HP'])