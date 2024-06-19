#!/usr/bin/env python3
import urllib.request

def getHtml(url):
    html = urllib.request.urlopen(url).read()
    html = html.decode('utf-8')
    print(html)
    return html

Url = 'http://quote.eastmoney.com/stocklist.html'#东方财富网股票数据连接地址

html = getHtml(Url)
print(html)

