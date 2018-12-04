# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 21:14:02 2018

@author: bpou
"""

import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent" : "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

url = 'https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81/408485'
r = requests.get(url, headers=headers).content.decode('utf8')

print (r)

print(r.find("北京地铁1号线"))
#p1 = re.compile(r'href="/item\w+北京地铁')
#pattern = re.compile(r'/item/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
pattern = re.compile(u"/item/(.+?)\">北京地铁(.+?)线")
#print(re.match(pattern,"hello").group())
url=re.findall(pattern, r)
print (url)
print("hell")
a=u"我爱@糗百，你呢"
print(a)
b=re.findall (u"(.+?)@糗百(.+)",a,re.S)
print (b)