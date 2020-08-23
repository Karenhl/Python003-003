import scrapy
from bs4 import BeautifulSoup
from spiders.items import SpidersItem

class DoubanSpider(scrapy.Spider):
    # 定义爬虫的名字
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    # 起始的url列表
    start_urls = ['http://movie.douban.com/']

    # 默认的parse函数
    # def parse(self, response):
        # pass

    # 爬虫启动时，引擎自动调用该方法，并且只会调用一次，用于生成初始的请求对象（Request）
    # start_requests()方法读取start_urls列表中的url并生成Request对象，发送给引擎
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        for i in range(0, 10):
            url = f'https://movie.douban.com/top250?start={i*25}'
            # url 请求的网址
            # callback 回调函数，引擎会将下载好的页面（Response对象）发送给该方法进行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数
            yield scrapy.Request(url=url, callback=self.parse)

    # 解析函数
    def parse(self, response):
        items = []
        soup = BeautifulSoup(response.text, 'html.parser')
        title_list = soup.find_all('div', attrs="hd")
        for tags in title_list:
            item = SpidersItem()
            for atags in tags.find_all("a"):
                title = atags.find("span").text
                link = atags.get("href")
                item['title'] = title
                item['link'] = link
                items.append(item)
                yield scrapy.Request(url=link, meta={'item':item}, callback=self.parse_details)

    # 具体页面解析
    def parse_details(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', attrs='related-info').get_text().strip()
        item['content'] = content
        yield item