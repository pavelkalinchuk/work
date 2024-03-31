import requests
import xml.etree.ElementTree as ET


url = 'http://mosrepwbs01/FrontSvcRep/kiassvc.asmx'
option = {"Content-Type": "application/soap+xml; charset = utf-8"}
data_file = 'soap_data\\Auth.xml'

with open(data_file, 'r') as f:
    data = f'{f.read()}'
print(data)
responce = requests.post(url, data=data, headers=option)
print(responce)
responce = ET.fromstring(responce.text)
print(responce)
for i in responce:
    a = i.text
    print(a)
