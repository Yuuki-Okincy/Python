import scrapy


class NovelspiderSpider(scrapy.Spider):
    name = "novelSpider"
    allowed_domains = ["www.bdzw.org"]
    start_urls = ["https://www.bdzw.org/read/1314/292185/"]

    def parse(self, response):
        # 获取所有p标签的文本（返回列表）
        paragraphs = response.xpath('//*[@id="novelcontent"]//p[position() < last()]/text()').getall()

        # 合并为字符串
        novel_content = '\n'.join(paragraphs)

        print(novel_content)

        next_nrl = response.xpath('//*[@id="next"]/@href').get()

        if next_nrl:
            print(f"找到下一章，继续爬取: {next_nrl}")
            yield response.follow(next_nrl, callback=self.parse)

        else:
            print("🎉 小说爬取完成！")

        self.save_into_file(response,novel_content)

    def save_into_file(self,response,data):
        with open('novelSpider.txt', 'a',encoding='utf-8') as f:
            f.write(data)


    # def get_next_page(self,response):


