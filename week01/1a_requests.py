"""
使用简单的request库爬取豆瓣页面
"""

import requests

url = "https://movie.douban.com/top250"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
response = requests.get(url=url ,headers=headers)

print(response.status_code)
print(response.text)
