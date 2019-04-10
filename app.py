import coinmarketcap
import json

with open("index/data.json") as f:
    data = json.load(f)

print(data["key"])