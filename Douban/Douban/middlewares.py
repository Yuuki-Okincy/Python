# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import base64
import random

from .settings import USER_AGENT_LIST, PROXY_LIST


# useful for handling different item types with a single interface


# class RandomUserAgentMiddleware(object):
#     def process_request(self, request, spider):
#         ua= random.choice(USER_AGENT_LIST)
#         request.headers["User-Agent"] = ua

class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXY_LIST)

        if 'user_passwd' in proxy:
            # 对账户密码进行编码
            b64_up=base64.encode(proxy['user_passwd'].encode())
            # 设置认证
            request.headers['Proxy-Authorization']='Basic '+b64_up.decode()
            # 设置代理
            request.meta['proxy'] = proxy["ip_port"]
        else:
            request.meta['proxy'] = proxy["ip_port"]