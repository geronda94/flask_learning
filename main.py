import requests

res = requests.get('https://mail.ru')
print(res.text)
