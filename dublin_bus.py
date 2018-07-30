import json
import requests
from pprint import pprint as prettyprint

response = requests.get("https://data.smartdublin.ie/cgi-bin/rtpi/realtimebusinformation?stopid=7602&format=json")
json_data = response.json()

prettyprint(json_data)
