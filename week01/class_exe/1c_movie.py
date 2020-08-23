"""
使用简单的request库爬取豆瓣页面,
结合lxml解析页面，xpath提取数据，
pandas做数据处理
"""
import requests
import lxml.etree
import pandas as pd


url = "https://movie.douban.com/subject/1292052/"
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}

response = requests.get(url=url, headers=headers)

selector = lxml.etree.HTML(response.text)

name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
date = selector.xpath('//*[@id="info"]/span[10]/text()')
score = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
mydata = [name, date, score]
print(mydata)

movie1 = pd.DataFrame(data=mydata)

movie1.to_csv('./movie1.csv', encoding='utf-8', index=False, header=False)