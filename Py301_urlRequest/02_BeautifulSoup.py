#!/usr/bin/env python3
##!/usr/bin/python3
# -*- coding:utf-8 -*-

import urllib.request
import requests
from bs4 import BeautifulSoup

url='http://stock.jrj.com.cn/share,000830,gdhs.shtml'

response = requests.get(url,timeout=None)
#response = requests.get(url,headers=headers)
#response = urllib.request.urlopen(url)
soup = BeautifulSoup(response.content,'html.parser')

table = soup.find('table', attrs={'id': 'table-gegugudong'})
results = table.find_all('td')
print(results)
