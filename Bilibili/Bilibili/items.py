# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    video_author = scrapy.Field()
    video_title = scrapy.Field()
    video_time = scrapy.Field()
    video_coin = scrapy.Field()
    video_like = scrapy.Field()
    video_comment = scrapy.Field()
    video_share = scrapy.Field()
    video_fav = scrapy.Field()


    pass
