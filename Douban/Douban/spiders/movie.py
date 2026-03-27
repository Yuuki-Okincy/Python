import scrapy

from ..items import DoubanItem


class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        el_list = response.xpath('//*[@class="info"]')

        for el in el_list:
            item = DoubanItem()
            item['name']= el.xpath('./div[1]/a/span/text()').get()
            print(item['name'])
            yield item

            url = response.xpath('//span[@id="next"]/a/@href').get()
            if url !=None:
                url = response.urljoin(url)
                yield scrapy.Request(url=url)
#                 //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]
