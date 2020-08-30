import requests
from fake_useragent import UserAgent


ua = UserAgent(verify_ssl=False)
headers = {
    "user-agent": ua.random,
    "referer": "https://accounts.douban.com/passport/login?source=movie"
}

form_data = {
    "ck": "",
    "name": "1234",
    "password": "1234",
    "remember": False,
    "ticket": ""
}

s = requests.Session()
re = s.post(url="https://accounts.douban.com/j/mobile/login/basic", data=form_data, headers=headers)
print(re.cookies)
