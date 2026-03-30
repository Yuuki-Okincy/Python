import hashlib
import re
import time
import urllib

import requests
import json

from you_get.common import cookies

"""获取加密参数"""
token = "02b5a73af8ff185235263e2f0ffd52f0"
kw_list=['耐克','彪马']





for kw in kw_list:

    kw_encode = urllib.parse.quote(kw)

    n_params = ({
        "device": "HMA-AL00",
        "isBeta": "false",
        "grayHair": "false",
        "from": "nt_history",
        "brand": "HUAWEI",
        "info": "wifi",
        "index": "4",
        "rainbow": "",
        "schemaType": "auction",
        "elderHome": "false",
        "isEnterSrpSearch": "true",
        "newSearch": "false",
        "network": "wifi",
        "subtype": "",
        "hasPreposeFilter": "false",
        "prepositionVersion": "v2",
        "client_os": "Android",
        "gpsEnabled": "false",
        "searchDoorFrom": "srp",
        "debug_rerankNewOpenCard": "false",
        "homePageVersion": "v7",
        "searchElderHomeOpen": "false",
        "search_action": "initiative",
        "sugg": "_4_1",
        "sversion": "13.6",
        "style": "list",
        "ttid": "600000@taobao_pc_10.7.0",
        "needTabs": "true",
        "areaCode": "CN",
        "vm": "nw",
        "countryNum": "156",
        "m": "pc_sem",
        "page": 2,
        "n": 48,
        "q": kw_encode,
        "qSource": "url",
        "pageSource": "tbpc.pc_sem_alimama/a.search_downSideRecommend.d3",
        "tab": "all",
        "pageSize": "48",
        "totalPage": "100",
        "totalResults": "800000",
        "sourceS": "0",
        "sort": "_coefp",
        "filterTag": "",
        "service": "",
        "prop": "",
        "loc": "",
        "start_price": None,
        "end_price": None,
        "startPrice": None,
        "endPrice": None,
        "p4pIds": "1002732693563,810094208202,524361998079,1014017497456,654505615533,826338370345,671503653424,996904779312,717230512579,943282430020,789894436619,1010874662810,880985674947,1004287250172,1025379749439,941947354163,898847312758,789800918992,929469933936,1013828216270,1027750637759,892914582671,1001934955271,937225195152,640275348713,979687007116,935102330968,881268353654,749452786169,1007204839590,861001880960,872037239120,983598560410,907331142451,970622254878,1013434218385,1018662675171,886613541583,927476107353,1024472310251,1008289247774,1018919921476,1014197555097,1027133408502,940117124994,1020493236177,983476674522,1029290879608",
        "categoryp": "",
        "myCNA": "gdI3In72RVECAXjnZvEDKa6o",
        "clk1": "804186e269f1a17732a9b8cd6b6a70f1",
        "refpid": "mm_2898300158_3078300397_115665800437"
    })
    u = int(time.time() * 1000)
    s = "12574478"

    data = {
        "appId": "43356",
        "params": json.dumps(n_params, separators=(',', ':')),
    }
    n_data = json.dumps(data, separators=(',', ':'))
    string = token + "&" + str(u) + "&" + s + "&" + n_data
    headers = {
        # cookie  用户信息 常用于检测是否有登录账号
        'cookie': 't=0d45b2241cc5de5605cdb5b92f7757b8; cna=gdI3In72RVECAXjnZvEDKa6o; thw=cn; _tb_token_=ff859674b9777; cookie2=1a389e716e421cd162891e3780b8e77e; 3PcFlag=1774236268509; wk_cookie2=1c22cab40e53ce1647af94246d36e1cf; wk_unb=UUphy%2FeHvMowD%2Fm8yw%3D%3D; _hvn_lgc_=0; havana_lgc2_0=eyJoaWQiOjIyMDE1MjU2OTM0NTgsInNnIjoiYWUyZDlkNTZmYWIyNzgxYTQ2YWNlYzc1ODA2M2U4ZTIiLCJzaXRlIjowLCJ0b2tlbiI6IjFrV1V4VkFnY0F3UUQyNlZwRzVkamhnIn0; lgc=tb803185300; cancelledSubSites=empty; dnk=tb803185300; tracknick=tb803185300; sn=; mtop_partitioned_detect=1; _m_h5_tk=02b5a73af8ff185235263e2f0ffd52f0_1774774994387; _m_h5_tk_enc=2e578fcf4606c730d8f8155cd91c243a; _samesite_flag_=true; unb=2201525693458; uc1=cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie15=URm48syIIVrSKA%3D%3D&cookie21=UtASsssme%2BBq&existShop=false&pas=0&cookie14=UoYZbjLBjofckQ%3D%3D; uc3=lg2=URm48syIIVrSKA%3D%3D&nk2=F5RNZTlfaucdizs%3D&id2=UUphy%2FeHvMowD%2Fm8yw%3D%3D&vt3=F8dD29QBybqNTq03aew%3D; csg=b4a2d266; ultraCookieBase=1k6S5%2BcxkgQpZDoYF3XJxQOSgU4Re4nVcFtOxxosB9E93eR%2F6w4zecmAvdWomJdHN9sUyc3w7pU%2FYyosG5Y2HQ6%2FlC20iywWM4dOO06lM4JYrsjhegHzpswsHHRJc1J%2BGI7DpsQMqywLhRbCkZAF1e75x46T3qfehipju%2FKUzvpjeZ14a46e8S8Cc2eob7ff%2FofJO%2FyESWHlfi%2BbySMvK3aYt8Xb3BWaJTnkAfpnWPY5uldbXuUmaI4Ggw0b0dGAc34C7WiTQMRtCDd66iTJQo1x4N8%2BXy%2FtPkiPaSDfBzAMFAr01tTGvvjfUZaYjvJxXULHM4OGduXIv; cookie17=UUphy%2FeHvMowD%2Fm8yw%3D%3D; skt=16c9dd3ecb781544; existShop=MTc3NDc2NTI3NQ%3D%3D; uc4=nk4=0%40FY4GsvaDMHH78ft2mRQBsdZA7NbHIg%3D%3D&id4=0%40U2grEJAUx4Nh0bJTn%2BQld4btZDz0q80w; _cc_=Vq8l%2BKCLiw%3D%3D; _l_g_=Ug%3D%3D; sg=080; _nk_=tb803185300; cookie1=VWt8kDm9nyptZQml2AC66P6U3Xs%2B5QQKg7HNpNDN1Fg%3D; sgcookie=E1004QFSVZFjFwm0saPCPj%2BOiziIHZRewfXXER01U%2BSH545gMzvLC8XA3w4AviWtKBDf0t750icZq6WqYVIgMWjAo%2Bo5sIYibKrnZsEKUXU3pZM%3D; havana_lgc_exp=1805869276000; sdkSilent=1774794075999; havana_sdkSilent=1774794075999; xlly_s=1; tfstk=gvDxbjbwaUYmrqJWJtAoIgZ5sDKo6QmVeqoCIP4c143-x4t4sFo_fR3SSnzmfEutBziZiS2bS5Us-VEinADtaOnEbxx4Inyq0Ry6-evnWmo4Q9FSd4MTF8ZLDdqfGOw4FiKuPcJHKmofmotnVpccYBzuA16s5SN5Vo45cN6j5767bz6bftZ1P3EaPRZbGs_5Forbcoaj50t8jz6b5Vw628azfRas5RM1YnUPcoBtNDeh3UbceBREeoFYWO45BckhKSzCWr61Cr3gM6nbyO6sefTROpUXTg4anroYDVJF3-NtTcqtkKBjWDkryugBB94j4Dc3gx9F_WeuPWaSdZ1bv-UYOxNPvOo81bH8nxTNT0m8lWeoZQ80s-3xTyPXaUut2r0sH7_vrPcnqxN-RUX-75hEjl3vHtgC4DHnp72F-yEGG3KR_1Pb4oPP42dUfRa32yxbG15asur8-3KR_1Pb4uUHct1N_5qP.; isg=BNHRCjTbXCiVTLBEx0HNNW-u4N1rPkWw6YurXrNmzRi3WvGs-45VgH-4_C680t3o',
        'referer': 'https://uland.taobao.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'

    }
    url = 'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/'


    sign = hashlib.md5(string.encode('utf-8')).hexdigest()

    # 查询参数
    params = {
        'jsv': '2.7.2',
        'appKey': '12574478',
        't': u,
        'sign': sign,
        'api': 'mtop.relationrecommend.wirelessrecommend.recommend',
        'v': '2.0',
        'type': 'jsonp',
        'dataType': 'jsonp',
        'callback': 'mtopjsonp3',
        'data': n_data,

    }

    # 发送请求（增加异常处理）
    try:
        response = requests.get(url=url, params=params, headers=headers, timeout=10)
        response.raise_for_status()  # 抛出HTTP错误
        text = response.text
        print("\n接口返回结果：")

        # 解析JSONP结果（提取核心信息）
        if "FAIL_SYS_TOKEN_EMPTY" in text:
            print("\n❌ 错误：令牌为空，请更新有效的_m_h5_tk和token！")
        elif "SUCCESS" in text:
            print("\n✅ 接口调用成功！")
        else:
            print("\n⚠️  其他返回，请检查结果内容")

    except requests.exceptions.RequestException as e:
        print(f"\n❌ 请求失败：{e}")

    # 解析数据
    text_json = re.findall(r'mtopjsonp3\((.*)\)', text)[0]
    # 转成json字典数据
    json_data = json.loads(text_json)
    # 字典取值,提取商品信息所在的列表
    itemsArray = json_data['data']['itemsArray']
    # for循环遍历，提取列表里的元素
    for index in itemsArray:
        # 在循环中捕获每个商品信息内容，保存字典中
        try:
            dit = {
                '标题': index['title'].replace('<span class=H>', '').replace('</span>', ''),
                '价格': index['price'],
            }
            print(dit)
        except:
            pass


