from scrapy import Spider
from scrapy import Request
from scrapy import Selector


class no2spider(Spider):
    name = 'test'
    start_urls = ['http://www.peopel.com']

    def login_callback(self, response):
        print response.body
        for i in range(0,10):
            # yield Request('https://www.baidu.com/s?wd=scrapy&rsv_spt=1&rsv_iqid=0x95972e0500043875&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=4&rsv_sug1=3&rsv_sug7=100&rsv_t=ea02PHwrUpY5cGgSBcDUArlGex0QepcQ6cWEM58WmuJaR%2BqHaL8iw8VdYz8mEOcLYbdZ')
            print i


    def start_requests(self):
        'start requests:'
        for i in range(0,1):
            yield Request('https://www.tencent.com/zh-cn/index.html', method='GET', callback=self.login_callback)

    def parse(self, response):
      print response


if __name__ == '__main__':
    html = '<html><body><span>abc</span><span>def</span></body></html>'
    sel = Selector(text=html)
    nodes = sel.xpath('//span/text()')
    for i in nodes:
        print i.extract()
    nodes = sel.css('span')
    for i in nodes:
        print i.extract()