#coding=utf-8
import requests
import sys

def download(url, header):
    res = requests.get(url, headers=header)
    print res.encoding
    # res.encoding = 'utf-8'
    return res.text

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('UTF-8')  # 解决报错 asclli
    print 'hello boy'
    headers = {
        # "authority": "www.shodan.io",
        # "method": "GET",
        # "path": "/search?query=port%3A102",
        # "scheme": "https",
        "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Cache-control': 'max-age=0',
        'Cookie': '__jsluid=f6f417e8f3d85567104974004576ee0f; Hm_lvt_3c8266fabffc08ed4774a252adcb9263=1511271783; Hm_lpvt_3c8266fabffc08ed4774a252adcb9263=1511271796; __jsl_clearance=1511275317.335|0|9qpEaJXwrKDUTzn4PzDyPRFtk88%3D',
        'Referer': 'https://www.zoomeye.org/searchResult?q=port%3A102',
        'Host':'www.zoomeye.org',
        'Connection':'keep-alive',
        'Pragma':'no-cache',
        'Upgrade-Insecure-Requests': str(1),
        'Cache-Control':'no-cache',
        # 'User-Agent': 'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'
    };
    text = download('https://www.zoomeye.org/searchResult?q=port%3A102', headers)
    print text