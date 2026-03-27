import scrapy


class BookSpider(scrapy.Spider):
    name = "Book"
    allowed_domains = ["jd.com"]
    start_urls = ["https://book.jd.com/booksort.html"]

    def parse(self, response):
        # big_node_list=response.xpath('//div[@class="mc"]/dl/dt/a')
        big_node_list = response.xpath('//*[@id="booksort"]/div[2]/dl/dt/a')
        for big_node in big_node_list:
            big_category = big_node.xpath('./text()').extract_first()
            big_category_link = response.urljoin(big_node.xpath('./@href').extract_first())
            print(big_category, big_category_link)

