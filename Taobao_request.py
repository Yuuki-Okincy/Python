import hashlib
import re
import time
import urllib

import requests
import json

from you_get.common import cookies

"""获取加密参数"""
token = "867c6d0091c12c925af81722d6c6cec9"
kw_list=['耐克','彪马']

for kw in kw_list:
    print(kw)

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
    print(u)
    s = "12574478"

    data = {
        "appId": "43356",
        "params": json.dumps(n_params, separators=(',', ':')),
    }
    n_data = json.dumps(data, separators=(',', ':'))
    string = token + "&" + str(u) + "&" + s + "&" + n_data
    headers = {
        # cookie  用户信息 常用于检测是否有登录账号
        'cookie': 't=0d45b2241cc5de5605cdb5b92f7757b8; cna=gdI3In72RVECAXjnZvEDKa6o; thw=cn; xlly_s=1; _tb_token_=ff859674b9777; cookie2=1a389e716e421cd162891e3780b8e77e; 3PcFlag=1774236268509; wk_cookie2=1c22cab40e53ce1647af94246d36e1cf; wk_unb=UUphy%2FeHvMowD%2Fm8yw%3D%3D; sgcookie=E100mX9M1CXM4l7%2Fo0NJ%2Bk03lbUHyUc7TfJicNH5qW4kg8yDvD%2BjmxgfVpi3ck16WQG%2BvKNkh8I85bsiEJ2ZhD8ZgG%2B%2Fno3oSvAfVQFxzFgjtqU%3D; _hvn_lgc_=0; havana_lgc2_0=eyJoaWQiOjIyMDE1MjU2OTM0NTgsInNnIjoiYWUyZDlkNTZmYWIyNzgxYTQ2YWNlYzc1ODA2M2U4ZTIiLCJzaXRlIjowLCJ0b2tlbiI6IjFrV1V4VkFnY0F3UUQyNlZwRzVkamhnIn0; unb=2201525693458; csg=02793c52; lgc=tb803185300; cancelledSubSites=empty; cookie17=UUphy%2FeHvMowD%2Fm8yw%3D%3D; dnk=tb803185300; skt=90231dead882ddc5; tracknick=tb803185300; _l_g_=Ug%3D%3D; sg=080; _nk_=tb803185300; cookie1=VWt8kDm9nyptZQml2AC66P6U3Xs%2B5QQKg7HNpNDN1Fg%3D; uc1=cookie14=UoYZbjdDtjy9Gg%3D%3D&cookie15=WqG3DMC9VAQiUQ%3D%3D&cookie21=V32FPkk%2FgPzW&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&existShop=false&pas=0; sn=; uc3=vt3=F8dD29X8tjKZfteOQKU%3D&nk2=F5RNZTlfaucdizs%3D&id2=UUphy%2FeHvMowD%2Fm8yw%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; existShop=MTc3NDIzNjMxNA%3D%3D; uc4=nk4=0%40FY4GsvaDMHH78ft2mRQBsdOVuaPTMw%3D%3D&id4=0%40U2grEJAUx4Nh0bJTn%2BQld4btYYBONTjW; _cc_=W5iHLLyFfA%3D%3D; mtop_partitioned_detect=1; _m_h5_tk=867c6d0091c12c925af81722d6c6cec9_1774330619702; _m_h5_tk_enc=0857104e040c90a83a4367dfa07d518c; _samesite_flag_=true; havana_lgc_exp=1805426701411; sdkSilent=1774351501410; havana_sdkSilent=1774351501410; tfstk=g_wtbbTVTwbg-PWCydf3nRAdzUj3H6qwpPrWnq0MGyULqysZiZrjcxUQoGugcNzYH2Z4sfDsoj3brrn0I-2YTKEz0RjZnGkabxkfraXuklrZ3tI--owxdXirDtmjGdMZdhInRoWlElrs2Lh1vTViacuZVI9blfGCdmgIfFiblX9I029scdiXRMnqRxiXhmiBO0m6GhiblksK02iscrMfvvgEcxgblxMsPG3efcpYOSTPxB_RnLvupchtkK0BHl2BEfgWY29vHVhj6BEsJK9bpS_pNT31aH0qIVrtXrWyQAGYaomYWOp_kuyUJDa5HL0_YuVo_R6ygbHnRbgQFFOs2A3tNRGe2KrKGWeKIR_2akqK5bH3t67iiAUTa4l1TwzYvV4bBXTO-qVuxRGLPwvLujFzmmUOBda542eueXDyr4nD1MIpgIlsYcleYzCrcxgov4js1IRqiDoKrMIpgIlsYD3lfdO2gjmF.; isg=BBISz6txr298vdNh6IyeSKj7Y9j0Ixa9Th5Ie9xrPkWw77LpxLNmzRgFX0tTn45V',
        'referer': 'https://uland.taobao.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'

    }
    url = 'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/'


    sign = hashlib.md5(string.encode('utf-8')).hexdigest()
    print(sign)

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
    priceArray = json_data['data']['itemsArray']
    # for循环遍历，提取列表里的元素
    for index in priceArray:
        # 在循环中捕获每个商品信息内容，保存字典中
        try:
            dit = {
                '标题': index['title'].replace('<span class=H>', '').replace('</span>', ''),
                '价格': index['price'],
            }
            print(dit)
        except:
            pass


