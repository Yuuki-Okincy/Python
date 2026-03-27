import scrapy


class Git2Spider(scrapy.Spider):
    name = "git2"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/login"]

    def parse(self, response):
        # 从登录页面响应中解析出post数据
        token = response.xpath('//input[@name="authenticity_token"]/@value').get()

        post_data = {'commit':'sign in',
                     'utf-8':'√',
                     'authenticity_token':token,
                     'login':'3552057096@qq.com',
                     'password':'xhz20040817',
                     'webauthn-supported':'support',}
        yield scrapy.FormRequest(url='https://github.com/session',
                                 callback=self.after_login,
                                 formdata=post_data,)
    #     针对登录地址发送post请求
    def after_login(self, response):
        yield scrapy.Request(url='https://github.com/Yuuki-Okincy',callback=self.check_login)
        pass
    def check_login(self, response):
        print(response.xpath('/html/head/title/text()').get())