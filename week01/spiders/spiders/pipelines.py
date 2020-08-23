# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpidersPipeline:

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise Dropitem异常
    def process_item(self, item, spider):
        title = item['title']
        link = item['link']
        content = item['content']
        output = f'|{title}|\t|{link}|\t|{content}|\n'
        with open('./doubanmovies.txt', 'a+', encoding='utf-8') as f:
            f.write(output)
        return item
