import cloudscraper
import random

scraper = cloudscraper.create_scraper(interpreter='nodejs',delay=10,browser={
        'browser': 'chrome',
        'platform': 'android',
        'desktop': False
    })

cookie = scraper.get_cookie_string('https://dragontea.ink/')
print(cookie)
class crawler:
    def __init__(self, url,headers=None):
        self.url = url
        self.headers = headers

    def get(self):
        try:
            return scraper.get(self.url,proxies=self.getProxy()).content
        except:
            return None

    def getProxy(self):
        try:
            lines = tuple(open('checked.txt', 'r'))
            if len(lines) == 0:
                return None
            return {'http': random.choice(lines) }
        except:
            return None

    def post(self,data,headers):
        # try:
        print(token)
        return scraper.post(self.url,cookies=token,data=data,headers=headers or self.headers ,proxies=self.getProxy()).content
        # except:
        #     return None



