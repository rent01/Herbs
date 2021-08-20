'''
-*- coding: utf-8 -*-
@Author  : TY Ren
@Time    : 2021/8/12 10:06
@Software: PyCharm
@File    : HerbsRequest.py
'''

import requests
import urllib3
import urlencode
import time
from urllib.request import urlopen
urllib3.disable_warnings()

# 关键字Keyword查询，处理url,请求header
name = input("Herb name:")
params = {"st":"hn","qw":"name"}
url = 'https://tcmsp-e.com/portal/search?'
headers = {
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
  'Cookie': 'Hm_lvt_045f99afbec668d057769af796f1ed4f=1627869359; _ga=GA1.1.95170299.1627889797; session=eyJfZnJlc2giOmZhbHNlLCJjc3JmX3Rva2VuIjoiNzEwZjVkN2UyNWUwMWRmMDZlZDUzNjkwNzlhY2ZjZDc2NGZmOTAxZCJ9.YQoJ2Q.JyTrMrN_KEwnRLvKSivnljq5IRg; PHPSESSID=3ccf2d5443f4ac29653fe277c5564264; Hm_lpvt_045f99afbec668d057769af796f1ed4f=1629251793; _ga_Y7GC5FHYTY=GS1.1.1629249004.20.1.1629251820.0',
   'Host': 'tcmsp-e.com',
    #'Referer':'https://tcmsp-e.com/portal/search?st=hn&qw=%E5%BD%93%E5%BD%92'
 }
time.sleep(10)

# session = requests.session()
# session.headers = headers
# requests.utils.add_dict_to_cookiejar(session.cookies,cookie)
# res =session.get(url)

#对指定url发出请求，携带参数：
response = requests.get(url, headers = headers,params=params,verify= False)
page_text = response.text

# response.encoding = 'utf-8'
print(page_text)
file_name = name+'.html'
with open(file_name,'w',encoding='utf-8') as fp:
    fp.write(page_text)
