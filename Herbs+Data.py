'''
-*- coding: utf-8 -*-
@Author  : TY Ren
@Time    : 2021/8/18 9:30
@Software: PyCharm
@File    : Herbs+Data.py
'''
#===================================
# This is the database for all herbs
#===================================

import requests
import time
import pandas as pd
from lxml import html
from lxml import etree
import re

# 检查所有Sheet名字
# xl = pd.ExcelFile('TCMSP.xlsx')
# print(xl.sheet_names)

# 使用pandas读取TCMSP的excel文件
data = pd.read_excel('TCMSP.xlsx', sheet_name= 0)
print('表格属性：',data.shape)    #表格有几行几列
print('表格列名：',data.columns)  #表格有哪些列名
print('--------------------------------------分割线-------------------------------------')
print('表格前五行：',data.head(6))
print('表格后五行：',data.tail(6))

cname = data['Chinese name']
print(cname)
for cn in cname:
 # print(re.split("\(",cn)[0])
 name = re.split("\(",cn)[0]
 time.sleep(2)

 ## 关键字Keyword查询，处理url,请求header
 # name= input("关键字:")
 param = {"st":"hn","qw":name}
 url = 'https://tcmsp-e.com/portal/search?st=hn&qw=name'
 headers = {
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
   'Cookie':'Hm_lvt_045f99afbec668d057769af796f1ed4f=1627869359; _ga=GA1.1.95170299.1627889797; session=eyJfZnJlc2giOmZhbHNlLCJjc3JmX3Rva2VuIjoiNzEwZjVkN2UyNWUwMWRmMDZlZDUzNjkwNzlhY2ZjZDc2NGZmOTAxZCJ9.YQoJ2Q.JyTrMrN_KEwnRLvKSivnljq5IRg; PHPSESSID=3ccf2d5443f4ac29653fe277c5564264; Hm_lpvt_045f99afbec668d057769af796f1ed4f=1629360713; _ga_Y7GC5FHYTY=GS1.1.1629360712.28.1.1629360723.0',
    'Host': 'tcmsp-e.com',
     'Referer':'https://tcmsp-e.com/portal/search?st=hn&qw=chenpi'
  }
 time.sleep(10)

 #对指定url发出请求，携带参数：
 response = requests.get(url, headers = headers, params= param,verify= False)
 page_text = response.text
 #
 # # 以下为获取网页中excel思路，通过etree获取？
 # # s= etree.HTML(response.text)
 # # ingre = s.xpath('//*[@id="ingredients"]/div[1]/a[1]/text()')
 # # print(ingre)
 #
 response.encoding = 'utf-8'
 print(page_text)
 file_name =name+'.html'
 with open(file_name,'w',encoding='utf-8') as fp:
     fp.write(page_text)

