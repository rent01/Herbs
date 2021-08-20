'''
-*- coding: utf-8 -*-
@Author  : TY Ren
@Time    : 2021/8/17 12:20
@Software: PyCharm
@File    : Wechat.py
'''
import time
import requests
import json
for i in range(1,20):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63030522)',
             'Cookie': 'wxuin=136194475; lang=zh_CN; rewardsn=; wxtokenkey=777; appmsg_token=1126_0F9duYocqnRCQA8aS-oTf8GStBlAxysKrdWCcedY7LfuNCp-aqpeTSTGBOA~; devicetype=iPhoneiOS13.5.1; version=17001233; pass_ticket=PgxVpwDa7fOQs0XmUVQhpmbNz9E1fOm7NVn/y4tF713hAl7z21MogW9XWfPkVB; wap_sid2=CKvT+EASigF5X0hENVZaZDBMSkptbnk0WW9LdlJEaFZLTGhVR1R2ajNyTDA2YkdjVW4tblR2ZU80c2NzS1VxZjRXa0s3YVhBVTV6S2hnd3VsR2RjN1QzWGJ1RFEyTVFETjAzWF9XRmsxcWpIeEdWcmRhdWltMURQVHNRVHFuZDRxLVFocXd6azZqbFVRU0FBQX4wnaTtiAY4DUCVTg==',
             'Host': 'mp.weixin.qq.com',
             'Referer': 'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzIxNjc2MTc2MQ==&scene=124&uin=MTM2MTk0NDc1&key=1b8ee8087b452ef1ffe573b64c127ccde8f2ae78f3554fb62ab5e0d6871a64de90670a6278131aa7b504688dc7812e8928499540bf30bb3b73fa5036b06546a83091ce4f8aff99fa17f06cc161883c4b017ed303029de7fd47bacb073610af23c924aeec2fb7bab962a9991c6f17f11bf7add5fcf5c74a3a452584d2be90af81&devicetype=Windows+10+x64&version=63030522&lang=zh_CN&a8scene=7&pass_ticket=PgxVpwDa7fOQ%2Bs0XmUVQhpmbNz9E1fOm7NVn%2Fy4tF713hAl7z21Mo%2BgW9XWfPkVB&fontgear=1'}
    url = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzIxNjc2MTc2MQ==&f=json&offset='+str(i*10)+'&count=10&is_ok=1&scene=124&uin=MTM2MTk0NDc1&key=1b8ee8087b452ef1ffe573b64c127ccde8f2ae78f3554fb62ab5e0d6871a64de90670a6278131aa7b504688dc7812e8928499540bf30bb3b73fa5036b06546a83091ce4f8aff99fa17f06cc161883c4b017ed303029de7fd47bacb073610af23c924aeec2fb7bab962a9991c6f17f11bf7add5fcf5c74a3a452584d2be90af81&pass_ticket=PgxVpwDa7fOQ%2Bs0XmUVQhpmbNz9E1fOm7NVn%2Fy4tF713hAl7z21Mo%2BgW9XWfPkVB&wxtoken=&appmsg_token=1126_opAIloIO3FHh%252FuAYAEpMUUUYe_q8c9qkg6K76Q~~&x5=0&f=json'
    url ='https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzIxNjc2MTc2MQ==&f=json&offset='+str(i*10)+'&count=70&is_ok=1&scene=124&uin=MTM2MTk0NDc1&key=9b9742add22a229fb8672b466bfc47020599904fb5476feee5e704b662a93fbe6a64c42ff8b71e5dde6027dbe08a4f4c65a91086e4af881fd0d59f5b4c6e25988f87ab34376848067ad29ba1f83e48e58d4743307f60bf81f696d5f624cfccc7b0400ef7bb8cbec014e43f800471fce23b5b8217003fb7f627691faabd51299a&pass_ticket=PgxVpwDa7fOQ%2Bs0XmUVQhpmbNz9E1fOm7NVn%2Fy4tF713hAl7z21Mo%2BgW9XWfPkVB&wxtoken=&appmsg_token=1126_sPoiRikxGasdVUWDAtbuxgMRbCsOfYZqlzxa-Q~~&x5=0&f=json'
    print(url)
    time.sleep(20)
    res = requests.get(url,headers=headers)
    print(res.json())
    jd = res.json()
    for j in range(1,10):
        print(json.loads(jd['general_msg_list'])['list'][j]['app_msg_ext_info']['title'])






# import requests
# import json
# for i in range(5,10):
#     headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63030522)',
#              'Cookie': 'wxuin=136194475; lang=zh_CN; rewardsn=; wxtokenkey=777; appmsg_token=1126_0F9duYocqnRCQA8aS-oTf8GStBlAxysKrdWCcedY7LfuNCp-aqpeTSTGBOA~; devicetype=iPhoneiOS13.5.1; version=17001233; pass_ticket=PgxVpwDa7fOQs0XmUVQhpmbNz9E1fOm7NVn/y4tF713hAl7z21MogW9XWfPkVB; wap_sid2=CKvT+EASigF5X0hENVZaZDBMSkptbnk0WW9LdlJEaFZLTGhVR1R2ajNyTDA2YkdjVW4tblR2ZU80c2NzS1VxZjRXa0s3YVhBVTV6S2hnd3VsR2RjN1QzWGJ1RFEyTVFETjAzWF9XRmsxcWpIeEdWcmRhdWltMURQVHNRVHFuZDRxLVFocXd6azZqbFVRU0FBQX4wnaTtiAY4DUCVTg==',
#              'Host': 'mp.weixin.qq.com',
#              'Referer': 'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzIxNjc2MTc2MQ==&scene=124&uin=MTM2MTk0NDc1&key=1b8ee8087b452ef1ffe573b64c127ccde8f2ae78f3554fb62ab5e0d6871a64de90670a6278131aa7b504688dc7812e8928499540bf30bb3b73fa5036b06546a83091ce4f8aff99fa17f06cc161883c4b017ed303029de7fd47bacb073610af23c924aeec2fb7bab962a9991c6f17f11bf7add5fcf5c74a3a452584d2be90af81&devicetype=Windows+10+x64&version=63030522&lang=zh_CN&a8scene=7&pass_ticket=PgxVpwDa7fOQ%2Bs0XmUVQhpmbNz9E1fOm7NVn%2Fy4tF713hAl7z21Mo%2BgW9XWfPkVB&fontgear=1'}
#     url = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzIxNjc2MTc2MQ==&f=json&offset='+str(i*10)+'&count=10&is_ok=1&scene=124&uin=MTM2MTk0NDc1&key=1b8ee8087b452ef1ffe573b64c127ccde8f2ae78f3554fb62ab5e0d6871a64de90670a6278131aa7b504688dc7812e8928499540bf30bb3b73fa5036b06546a83091ce4f8aff99fa17f06cc161883c4b017ed303029de7fd47bacb073610af23c924aeec2fb7bab962a9991c6f17f11bf7add5fcf5c74a3a452584d2be90af81&pass_ticket=PgxVpwDa7fOQ%2Bs0XmUVQhpmbNz9E1fOm7NVn%2Fy4tF713hAl7z21Mo%2BgW9XWfPkVB&wxtoken=&appmsg_token=1126_opAIloIO3FHh%252FuAYAEpMUUUYe_q8c9qkg6K76Q~~&x5=0&f=json'
#     url ='https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzIxNjc2MTc2MQ==&f=json&offset='+str(i*10)+'&count=70&is_ok=1&scene=124&uin=MTM2MTk0NDc1&key=9b9742add22a229fb8672b466bfc47020599904fb5476feee5e704b662a93fbe6a64c42ff8b71e5dde6027dbe08a4f4c65a91086e4af881fd0d59f5b4c6e25988f87ab34376848067ad29ba1f83e48e58d4743307f60bf81f696d5f624cfccc7b0400ef7bb8cbec014e43f800471fce23b5b8217003fb7f627691faabd51299a&pass_ticket=PgxVpwDa7fOQ%2Bs0XmUVQhpmbNz9E1fOm7NVn%2Fy4tF713hAl7z21Mo%2BgW9XWfPkVB&wxtoken=&appmsg_token=1126_sPoiRikxGasdVUWDAtbuxgMRbCsOfYZqlzxa-Q~~&x5=0&f=json'
#     print(url)
#     res = requests.get(url,headers=headers)
#     print(res.json())
#     jd = res.json()
#     for j in range(1,11):
#         print(json.loads(jd['general_msg_list'])['list'][j]['app_msg_ext_info']['title'])