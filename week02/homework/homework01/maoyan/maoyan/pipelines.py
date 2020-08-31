# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class MaoyanPipeline:
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_cates = item['movie_cates']
        movie_date = item['movie_date']

        try:
            conn = pymysql.connect(
                host = "localhost",
                port = 3306,
                user = 'root',
                password = '123456',
                db = 'test',
                charset = "utf8mb4"
            )

            cur = conn.cursor()
            # print(type(movie_date))

            sql = 'insert into movie_table values (\"{}\",\"{}\",\"{}\");'.format(movie_name, movie_cates, movie_date)
            # print(sql)
            cur.execute(sql)
            conn.commit()

        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            cur.close()
            conn.close()

        return item
