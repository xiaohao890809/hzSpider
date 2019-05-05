import urllib.parse

a = "baidu.com/m?k=123"
b = "m?k=45345346"
print(urllib.parse.urljoin(a, b ))