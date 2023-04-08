import requests

res = requests.get('http://127.0.0.1:8000/cars/').json()
# print(res)
for r in res:
    print(r['username'])
    