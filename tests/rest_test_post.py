from importlib.resources import contents
import json
from urllib import response
from xml.etree.ElementTree import indent
import requests
import json

with open('request.json', 'r') as read_file:
    data = json.load(read_file)

r = requests.post('https://reqres.in/api/users', data=data)
responce = json.loads(r.content)
# Вывод в консоль
responce_term = json.dumps(responce, indent=4)
print("\n", responce_term, "\n")
# Вывод в файл
with open('responce.json', 'w') as write_file:
    json.dump(responce, write_file, indent=4)
