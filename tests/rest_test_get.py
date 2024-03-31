import requests

r = requests.get('https://reqres.in/api/users?page=2')
print("\n"*2, r._content, "\n"*2)
