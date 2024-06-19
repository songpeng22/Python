import urllib, requests
import time

#result = urllib.request.getproxies()
#print(result)
result = requests.get("http://www.google.com")
print(result)
time.sleep(0.6)
result = requests.get("https://www.google.com/search?newwindow=1&sca_esv=b6768ec4eb9a166c&hl=zh-TW&sxsrf=ADLYWILwhPKN280hskE_MfltV2llZSRGZg:1718349584726&q=%E8%8D%AF%E7%9B%92+%E4%B8%89%E6%9C%9F&udm=2&fbs=AEQNm0AaBOazvTRM_Uafu9eNJJzC3QMRKTS5UIeA1ZwBo3sfI5tRK2wzmp0oTr82Uvr9kDXiTRz3gA0DDfNNOgYCYNjBcmw54O9frJiaK1tlHSUR_HWF1fBfgmNdaLk4P6LppqlDUx8zHneKwUigw3LRz0dvWu1lqyijCzufjJaNtW4NyQMHVV6_iI-2OI4NvvXkHHBV5ib3&sa=X&ved=2ahUKEwj5zOOEx9qGAxVLQEEAHTXTDG4QtKgLegQIChAB&biw=1707&bih=898&dpr=1.5")
print(result)
html = result.text
print(html)
