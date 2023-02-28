from requests_html import HTMLSession


session = HTMLSession()
res = session.get('https://mail.ru')
print(res.text)
