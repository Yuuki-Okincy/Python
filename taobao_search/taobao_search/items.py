# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):
    # define the fields for your item here like:
    # 定义要存MySQL的字段
    keyword = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    pass
