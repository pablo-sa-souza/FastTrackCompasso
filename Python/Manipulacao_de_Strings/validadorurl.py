import re

url = 'dasdsad'
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError ("a url não é valida")
else:
    print("é valida")