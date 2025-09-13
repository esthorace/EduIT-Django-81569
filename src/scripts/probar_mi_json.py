import requests

response = requests.get("http://127.0.0.1:8000/mi_json/")
datos = response.json()
for item in datos:
    print(item)
