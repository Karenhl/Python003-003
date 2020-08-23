# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    
    movie_name = scrapy.Field()
    movie_cates = scrapy.Field()
    movie_release_date = scrapy.Field()
