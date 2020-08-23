# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanPipeline:
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_cates = item['movie_cates']
        movie_release_date = item['movie_release_date']
        
        # 把字段整合到一个字符串中
        output = f'|{movie_name}|\t|{movie_cates}|\t|{movie_release_date}|\n\n'

        with open('./maoyanmovie.txt', 'a+', encoding='utf-8') as f:
            f.write(output)
        return item
