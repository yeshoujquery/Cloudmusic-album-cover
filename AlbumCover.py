import requests
from lxml import etree
import sys

class albumCover():
    url = ''
    headers = {'Host': 'music.163.com',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Referer': 'http://music.163.com/',
               'Accept-Encoding': 'gzip, deflate, sdch',
               'Accept-Language': 'zh-CN,zh;q=0.8'
               }

    def __init__(self, url):
        self.url = "".join(url.split("#/"))

    def load(self):
        try:
            page = requests.get(self.url, headers=self.headers)
            content = etree.HTML(page.text)
            img_url = content.xpath("//img[@class='j-img']/@data-src")
            name = content.xpath("//em[@class='f-ff2']/text()")
            self.download(img_url[0], name[0])
        except Exception as e:
            print(e)

    def download(self, urls, name):
        page = requests.get(urls)
        with open('%s.jpg' % name, 'wb') as fd:
            for chunk in page.iter_content(100):
                fd.write(chunk)

if __name__ == '__main__':
    url = sys.argv[1]
    if url:
        AC = albumCover(url)
        AC.load()
