import requests

r = requests.get("https://github.com")
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)


r = requests.post("http://httpbin.org/post", data={'key': 'value'})
print(r.json())