import requests


urls = "http://127.0.0.1:8000/stuinfo"

r = requests.get(url=urls)

data = r.json()

print(data)