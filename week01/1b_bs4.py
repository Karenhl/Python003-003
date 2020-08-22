"""
使用简单的request库爬取豆瓣页面,
并结合BeautifulSoup提取数据
"""

import requests
from bs4 import BeautifulSoup as bs

url = "https://movie.douban.com/top250"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
response = requests.get(url=url ,headers=headers)

b_html = bs(response.text,"html.parser")

for tags in b_html.find_all("div", attrs="hd"):
    for atags in tags.find_all("a"):
        # 打印a标签的href值
        print(atags.get("href"), end="\t")
        # 打印电影名字
        print(atags.find("span").text)



