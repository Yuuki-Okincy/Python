# -*- coding: utf-8 -*-
"""
直接运行Scrapy爬虫的脚本，可以在PyCharm中直接执行
"""
import os
import sys
import subprocess

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 导入Scrapy相关模块
from scrapy.cmdline import execute

if __name__ == '__main__':
    try:
        # 运行爬虫
        execute(['scrapy', 'crawl', 'bili'])
    except Exception as e:
        print(f"爬虫运行出错: {e}")
        import traceback
        traceback.print_exc()