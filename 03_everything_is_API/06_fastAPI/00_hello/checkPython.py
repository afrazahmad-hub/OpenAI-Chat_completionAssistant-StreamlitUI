import requests

# Server must be up while requesting this way
res = requests.get('http://127.0.0.1:8000/')

print(res.text)
print(res.status_code)
print(res.headers)
print(res.json())