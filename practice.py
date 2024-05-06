import requests

url = 'http://127.0.0.1:5000/predict'  


data = {'text': 'The customer support is terrible. They never respond to my inquiries'}


response = requests.post(url, json=data)


print(response.json())
