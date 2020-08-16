import requests

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15"

header = {"user-agent": user_agent}

myurl = "https://movie.douban.com/top250"

response = requests.get(myurl, headers=header)

print(response.text)
print("返回码是", int(response.status_code))


