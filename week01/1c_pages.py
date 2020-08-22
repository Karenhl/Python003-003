"""
自动翻页
"""
import requests
from bs4 import BeautifulSoup as bs

# 获取每一页的数据
def get_page_data(url):

    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
    response = requests.get(url=url, headers=headers)

    bs_html = bs(response.text,"html.parser")

    for tags in bs_html.find_all("div", attrs="hd"):
        for atags in tags.find_all("a"):
            print(atags.get("href"), end='\t')
            print(atags.find("span").text)


def main():
    for i in range(0,250,25):
        url = "https://movie.douban.com/top250?start={}&filter=".format(i)
        # print(url)
        get_page_data(url)

    
if __name__ == '__main__':
    main()
