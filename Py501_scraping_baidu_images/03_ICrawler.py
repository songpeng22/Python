from icrawler.builtin import BaiduImageCrawler 
from icrawler.builtin import BingImageCrawler 
from icrawler.builtin import GoogleImageCrawler
from icrawler.utils import ProxyPool,Proxy
from icrawler import ImageDownloader
from six.moves.urllib.parse import urlparse
import base64
from icrawler import ImageDownloader
from icrawler.builtin import GreedyImageCrawler, GreedyParser

"""
parser_threads：解析器线程数目，最大为cpu数目
downloader_threads：下载线程数目，最大为cpu数目
storage：存储地址，使用字典格式。key为root_dir
keyword:浏览器搜索框输入的关键词
max_num:最大下载图片数目
"""

#batch MFG EXP
#生产日期 保质期 批号
#药盒 三期
#medicine box production date
#药盒 生产批号
#medicine box LOT
#tranquillonin - 安定宁'
#Flufloxacin - 氟氧沙星
#Tadalafil  - 他达拉非
#金柴清热颗粒 日期

#定制爬虫
"""

g_bFirst = False
g_file_idx = 0
class MyImageDownloader(ImageDownloader):
    def get_filename(self, task, default_ext):
        print("get_filename()...")
        url_path = urlparse(task["file_url"])[2]
        if "." in url_path:
            extension = url_path.split(".")[-1]
            if extension.lower() not in ["jpg", "jpeg", "png", "bmp", "tiff", "gif", "ppm", "pgm"]:
                extension = default_ext
        else:
            extension = default_ext
        file_idx = self.fetched_num + self.file_idx_offset
        #
        print(f"file_idx:{file_idx:06d}")
        #
        if(not g_bFirst):
            g_bFirst = True
            g_file_idx = 0
        else:
            g_file_idx = g_file_idx + 1
        return f"{g_file_idx:06d}.{extension}"
"""

class MyImageDownloader(ImageDownloader):

    def get_filename(self, task, default_ext):
        url_path = urlparse(task['file_url'])[2]
        if '.' in url_path:
            extension = url_path.split('.')[-1]
            if extension.lower() not in [
                    'jpg', 'jpeg', 'png', 'bmp', 'tiff', 'gif', 'ppm', 'pgm'
            ]:
                extension = default_ext
        else:
            extension = default_ext
        # works for python3
        filename = base64.b64encode(url_path.encode()).decode()
        return '{}.{}'.format(filename, extension)
#class MyCrawler(BingImageCrawler):
#class MyCrawler(GoogleImageCrawler):
#class MyCrawler(BaiduImageCrawler):
class MyBingCrawler(BingImageCrawler):
    def set_proxy_pool(self):
        self.proxy_pool = ProxyPool()
        #self.proxy_pool.scan(region='overseas', expected_num=10) # ERR
        self.proxy_pool.add_proxy(Proxy('http://127.0.0.1:7890', 'https')) # OK
        #self.proxy_pool.add_proxy(Proxy('http://192.168.10.77:7890', 'https')) # OK
        #self.proxy_pool.default_scan(region='overseas', expected_num=10, out_file='proxies.json')
class MyGoogleCrawler(GoogleImageCrawler):
    def set_proxy_pool(self):
        self.proxy_pool = ProxyPool()
        #self.proxy_pool.scan(region='overseas', expected_num=10) # ERR
        self.proxy_pool.add_proxy(Proxy('http://127.0.0.1:7890', 'https')) # OK
        #self.proxy_pool.add_proxy(Proxy('http://192.168.10.77:7890', 'https')) # OK
        #self.proxy_pool.default_scan(region='overseas', expected_num=10, out_file='proxies.json')
class MyBaiduCrawler(BaiduImageCrawler):
    def set_proxy_pool(self):
        self.proxy_pool = ProxyPool()
        #self.proxy_pool.scan(region='overseas', expected_num=10) # ERR
        self.proxy_pool.add_proxy(Proxy('http://127.0.0.1:7890', 'https')) # OK
        #self.proxy_pool.add_proxy(Proxy('http://192.168.10.77:7890', 'https')) # OK
        #self.proxy_pool.default_scan(region='overseas', expected_num=10, out_file='proxies.json')

my_storage = {'root_dir': 'E:\\Python\\Py501_scraping_baidu_images\\images'}
myBingcrawler = MyBingCrawler(downloader_cls=MyImageDownloader,
                            parser_threads=4, 
                            downloader_threads=4, 
                            storage=my_storage)
myGooglecrawler = MyGoogleCrawler(downloader_cls=MyImageDownloader,
                            parser_threads=4, 
                            downloader_threads=4, 
                            storage=my_storage)
myBaiducrawler = MyBaiduCrawler(downloader_cls=MyImageDownloader,
                            parser_threads=4, 
                            downloader_threads=4, 
                            storage=my_storage)
keyword_head= '地氯雷他定'
number = 50

myBingcrawler.crawl(keyword=keyword_head + ' 生产日期', 
                     max_num=number)
myGooglecrawler.crawl(keyword=keyword_head + ' 生产日期', 
                     max_num=number)
myBaiducrawler.crawl(keyword=keyword_head + ' 生产日期', 
                     max_num=number)

myBingcrawler.crawl(keyword=keyword_head + ' 保质期', 
                     max_num=number)
myGooglecrawler.crawl(keyword=keyword_head + ' 保质期', 
                     max_num=number)
myBaiducrawler.crawl(keyword=keyword_head + ' 保质期', 
                     max_num=number)

myBingcrawler.crawl(keyword=keyword_head + ' 批号', 
                     max_num=number)
myGooglecrawler.crawl(keyword=keyword_head + ' 批号', 
                     max_num=number)
myBaiducrawler.crawl(keyword=keyword_head + ' 批号', 
                     max_num=number)
"""                     
keyword_head= 'Desloratadine'
myBingcrawler.crawl(keyword=keyword_head + ' LOT', 
                     max_num=number)
myGooglecrawler.crawl(keyword=keyword_head + ' LOT', 
                     max_num=number)
myBaiducrawler.crawl(keyword=keyword_head + ' LOT', 
                     max_num=number)
myBingcrawler.crawl(keyword=keyword_head + ' MFD', 
                     max_num=number)
myGooglecrawler.crawl(keyword=keyword_head + ' MFD', 
                     max_num=number)
myBaiducrawler.crawl(keyword=keyword_head + ' MFD', 
                     max_num=number)
"""


"""

#百度图片爬虫
baidu_storage = {'root_dir': 'E:\\Python\\Py501_scraping_baidu_images\\\images'}

baidu_crawler = BaiduImageCrawler(parser_threads=2,
                                  downloader_threads=4,
                                  storage=baidu_storage)
baidu_crawler.crawl(keyword='他达拉非 生产日期', 
                    max_num=500)
"""
"""

#必应图片爬虫
bing_storage = {'root_dir': 'E:\\Python\\Py501_scraping_baidu_images\\images'}
bing_crawler = BingImageCrawler(parser_threads=2,
                                downloader_threads=4, 
                                storage=bing_storage)
bing_crawler.crawl(keyword='medicine box LOT',
                   max_num=500)
"""


"""

#谷歌图片爬虫
google_storage = {'root_dir': 'E:\\Python\\Py501_scraping_baidu_images\\images'}
google_crawler = GoogleImageCrawler(parser_threads=4, 
                                   downloader_threads=4, 
                                   storage=google_storage)
google_crawler.crawl(keyword='medicine box LOT', 
                     max_num=500)
"""

"""
def main():
    crawler = MyCrawler(
        downloader_threads=2, storage={'root_dir': 'E:\\Python\\Python501_scraping_baidu_images\\images'})
    crawler.crawl(keyword='药盒 三期', max_num=10)


if __name__ == '__main__':
    main()

"""