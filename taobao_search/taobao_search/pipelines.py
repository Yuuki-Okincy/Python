# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

import pymysql

class TaobaoSearchPipeline:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='xiahongzhen0',
            db='taobao_db',
            charset='utf8mb4'
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        print("🔥 进入管道，准备写入MySQL")

        try:
            sql = """
            INSERT IGNORE INTO goods (keyword, title, price)
            VALUES (%s, %s, %s)
            """
            data = (
                item['keyword'],
                item['title'],
                item['price']
            )

            self.cursor.execute(sql, data)
            self.conn.commit()
            print(f"✅ 写入MySQL成功：{item['title']}")

        except Exception as e:
            print(f"❌ 写入失败：{e}")

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()