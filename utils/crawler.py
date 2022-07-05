import cloudscraper
from fp.fp import FreeProxy
import requests

scraper = cloudscraper.create_scraper(interpreter='nodejs',delay=10,browser={
        'browser': 'chrome',
        'platform': 'android',
        'desktop': False
    })


class crawler:
    def __init__(self, url,headers=None):
        self.url = url
        self.headers = headers

    def get(self):
        return scraper.get(self.url,headers=self.headers).content #,proxies=self.getProxy()).content

    def getProxy(self):
        try:
            proxy = FreeProxy(rand=True,timeout=0.3).get()
            # print(proxy)
            return {'http':proxy}
        except:
            return None

    def post(self,data,headers):
        # requests.post(self.url,data=data,headers=self.headers)
        return scraper.post(self.url,data=data,headers=headers).content



