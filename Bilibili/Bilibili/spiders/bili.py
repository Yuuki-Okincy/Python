import json
import os
import re
import subprocess

import scrapy
# import re
# import requests
# import json
# import os
# import subprocess

from ..items import BilibiliItem

class BiliSpider(scrapy.Spider):
    name = "bili"
    # allowed_domains = ["www.bilibili.com"]
    allowed_domains = ["www.bilibili.com", "api.bilibili.com", "upos-sz-mirrorcos.bilivideo.com"]
    start_urls = ["https://www.bilibili.com/"]

    def __init__(self):
        self.all_videos = []
        self.video_save_dir = "bilibili_videos"
        # "换一换"计数
        self.change_count = 0
        self.max_changes = 5  # 最多换几次

    # 视频保存目录
    # video_save_dir = "bilibili_videos"


    def closed(self, reason):
        # 爬虫结束时一次性写入
        with open('bili_video.json', 'w', encoding='utf-8') as f:
            json.dump(self.all_videos, f, ensure_ascii=False, indent=10)

    def parse(self, response):
        # 从首页获取视频卡片链接
        video_url_list = response.xpath("//a[@class='bili-video-card__image--link']/@href").extract()

        # 处理每个视频链接
        for video_url in video_url_list:
            # if not video_url.startswith("http"):
            #     video_url = "https:" + video_url
             yield response.follow(video_url, callback=self.get_video_info)



    def get_video_info(self, response):


        video_info = BilibiliItem()
        video_info['video_title'] = response.xpath('//*[@id="viewbox_report"]/div[1]/div/h1/text()').extract_first()
        video_info['video_like'] = response.xpath('//*[@id="arc_toolbar_report"]/div[1]/div/div[1]/div/span/text()').extract_first()
        video_info['video_coin'] = response.xpath('//*[@id="arc_toolbar_report"]/div[1]/div/div[2]/div/span/text()').extract_first()
        video_info['video_fav'] = response.xpath('//*[@id="arc_toolbar_report"]/div[1]/div/div[3]/div/span/text()').extract_first()

        if share := response.xpath('//span[contains(@class, "video-share-info")]/text()').get():
            video_info['video_share'] = share.strip()
        else:
            video_info['video_share'] = ''

        if author := response.xpath('//a[contains(@class,"up-name")]/text()').get():
            video_info['video_author'] = author.strip()
        else:
            video_info['video_author'] = ''

        if time := response.xpath('//div[@class="pubdate-ip-text"]/text()').get():
            video_info['video_time'] = time.strip()
        else:
            video_info['video_time'] = ''

        video_info['video_comment'] = response.xpath('//div[@id="count"]/text()').get('无')


        # 获取视频BV号
        bv_id = response.url.split('/')[-1].split('?')[0]
        if bv_id.startswith('BV'):
            # 尝试下载视频
            self.download_video(bv_id, video_info['video_title'])

        self.all_videos.append(dict(video_info))
        
        yield video_info

    # 模拟换页
    def change_feet(self):