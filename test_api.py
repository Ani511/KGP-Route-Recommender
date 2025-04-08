import requests

data = {
    "starting_point": "Azad Hall",
    "destination": "Tech Market",
    "weights": [0.3, 0.2, 0.2, 0.1, 0.2]
}

response = requests.post("http://127.0.0.1:5000/get_best_route", json=data)

print(response.status_code)
print(response.text)
