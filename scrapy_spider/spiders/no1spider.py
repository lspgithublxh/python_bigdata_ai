#coding=utf-8
import scrapy

class no1spider(scrapy.Spider):
    name = 'no1spider'
    start_urls = [
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Books/'
        # 'http://www.people.com/',
        # 'http://www.tencent.com/'
    ]

    def parse(self, response):
        filename = response.url.split('/')[-2]
        print response.body
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
    # def start_requests(self): #返回一个Requests对象，是调用parse前返回的对象,实际封装了进行http请求的全部必要信息和回调信息


