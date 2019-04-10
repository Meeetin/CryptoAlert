import json
import pprint
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
with open("index/data.json") as f:
    data = json.load(f)
print(data["key"])

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
parameters = {
      'id' : '1,2',
     # 'convert': 'USD',
  }
headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': data["key"],
      'Accept-Encoding': 'deflate, gzip',
  }

session = Session()
session.headers.update(headers)
pp = pprint.PrettyPrinter(indent=4)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    pp.pprint(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    pp.pprint(e)