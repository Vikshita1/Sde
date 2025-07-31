import requests

url = "http://127.0.0.1:5000/api/products"
response = requests.get(url)
print(response.json())
