import requests


s = requests.Session()

s.get("http://httpbin.org/cookies/set/sessioncookie/123456789")
r = s.get("http://httpbin.org/cookies")
print(r.text)


with requests.Session as s:
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')