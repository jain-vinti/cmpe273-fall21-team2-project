import requests
url = 'http://localhost:8081'

with open('test.py', 'rb') as f:
    output = requests.post(url, data=f)

print(output.text)
