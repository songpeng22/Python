from icrawler.builtin import BaiduImageCrawler 
from icrawler.builtin import BingImageCrawler 
from icrawler.builtin import GoogleImageCrawler
from icrawler.utils import ProxyPool

"""
parser_threads：解析器线程数目，最大为cpu数目
downloader_threads：下载线程数目，最大为cpu数目
storage：存储地址，使用字典格式。key为root_dir
keyword:浏览器搜索框输入的关键词
max_num:最大下载图片数目
"""

#'药盒 三期'
#'medicine box production date'
#'药盒 生产批号'



"""

#必应图片爬虫
bing_storage = {'root_dir': 'E:\\Python\\Python501_scraping_baidu_images\\ICrawlerImages\\bing'}
bing_crawler = BingImageCrawler(parser_threads=2,
                                downloader_threads=4, 
                                storage=bing_storage)
bing_crawler.crawl(keyword='药盒 生产批号',
                   max_num=500)

"""
"""

#百度图片爬虫
baidu_storage = {'root_dir': 'E:\\Python\\Python501_scraping_baidu_images\\ICrawlerImages\\baidu'}

baidu_crawler = BaiduImageCrawler(parser_threads=2,
                                  downloader_threads=4,
                                  storage=baidu_storage)
baidu_crawler.crawl(keyword='生产日期', 
                    max_num=500)
"""

"""
"""
#谷歌图片爬虫
google_storage = {'root_dir': 'E:\\Python\\Python501_scraping_baidu_images\\ICrawlerImages\\google'}
google_crawler = GoogleImageCrawler(parser_threads=4, 
                                   downloader_threads=4, 
                                   storage=google_storage)
google_crawler.crawl(keyword='药 生产批号', 
                     max_num=500)


#定制爬虫
"""

class MyCrawler(GoogleImageCrawler):
    def set_proxy_pool(self):
        self.proxy_pool = ProxyPool()
        #self.proxy_pool.scan(region='overseas', expected_num=10)
        self.proxy_pool.default_scan(region='overseas', expected_num=10,
                                 out_file='proxies.json')

my_storage = {'root_dir': 'E:\\Python\\Python501_scraping_baidu_images\\ICrawlerImages\\images'}
my_crawler = MyCrawler(parser_threads=4, 
                                downloader_threads=4, 
                                storage=my_storage)
my_crawler.crawl(keyword='药盒 三期', 
                     max_num=500)
"""
"""
def main():
    crawler = MyCrawler(
        downloader_threads=2, storage={'root_dir': 'E:\\Python\\Python501_scraping_baidu_images\\ICrawlerImages\\images'})
    crawler.crawl(keyword='药盒 三期', max_num=10)


if __name__ == '__main__':
    main()

"""