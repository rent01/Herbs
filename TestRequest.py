'''
-*- coding: utf-8 -*-
@Author  : TY Ren
@Time    : 2021/8/12 9:58
@Software: PyCharm
@File    : TestRequest.py
'''

import requests
import urllib3
from urllib.request import urlopen
urllib3.disable_warnings()

url = 'https://www.baidu.com/s?'
# 此处可输入中药名：例如陈皮，常山等
kw = input("enter a word:")
param = {'wd':kw }

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
response = requests.get(url,headers=headers,params=param,verify=False)
page_text = response.text
# response.encoding = 'utf-8'
print(page_text)
file_name = kw+'.html'
with open(file_name,'w',encoding='utf-8') as fp:
    fp.write(page_text)
