import requests as rq

url = rq.get('http://api.open-notify.org/astros')
data = url.json()
print(data["number"])