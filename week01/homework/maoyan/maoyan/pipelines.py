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
        movie_date = item['movie_date']
        

        output = f'|{movie_name}|\t|{movie_cates}|\t|{movie_date}|\n'

        with open('./maoyanmovie.txt', 'a+', encoding='utf-8') as f:
            f.write(output)

        return item
