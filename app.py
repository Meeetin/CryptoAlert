import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
with open("index/data.json") as f:
    data = json.load(f)

print(data["key"])

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
      'start': '1',
      'limit': '2',
      'convert': 'USD',
  }
headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': data["key"],
  }

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)