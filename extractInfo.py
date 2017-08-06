import requests 
from bs4 import BeautifulSoup
import json 

with open('data.json') as data: 
    data = json.load(data) 

resp = requests.post(
  'https://www.deutschepost.de/sendung/simpleQueryResult.html',
  data=data
)
soup = BeautifulSoup(resp.text, 'html.parser')
resp_table = soup.find("div", { "class": "dp-table native-swipeable" })
print(resp_table.find_all("td", { "class": "grey" }))