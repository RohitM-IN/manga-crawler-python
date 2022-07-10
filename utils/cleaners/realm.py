import re
from utils.crawler import crawler
from utils.cleaners.common.mangastream import mangastream
from bs4 import BeautifulSoup

from utils.utils import fixUrl

class realm:
    def __init__(self, url):
        self.url = url
        self.html = crawler(self.url).get()
        self.parsed_html = BeautifulSoup(self.html,'html.parser')
        self.check404 = self.check404()
    
    def check404(self):
        if "Page not found" in self.parsed_html.title.get_text():
            return True
        return False

    def getList(self):
        data = mangastream(self.parsed_html).getList()

        return data

    def getManga(self):
        if self.check404 == True:
            return False
        ms = mangastream(self.parsed_html)

        chapters = self.parsed_html.find('div',{'class': 'eplister'}).find_all('li')

        details = self.parsed_html.find('div',{'class': 'tsinfo'})

        manga = {
            'title': ms.getMangaDetails(('h1',{'class': 'entry-title'}),"main-info").get_text(strip=True),
            'image': fixUrl(ms.getMangaDetails(('div',{'class': 'thumb'}),"info-left").find('img').get('src')),
            'description': ms.getMangaDetails(('div',{'class': 'entry-content'}),"info-right").get_text(strip=True),
            'genre': ms.getMangaGenreDetails(('span',{'class': 'mgen'})),
            'type': details.find(text=re.compile("Type")).next_sibling.get_text(strip=True),
            'status': details.find(text=re.compile("Status")).next_sibling.get_text(strip=True),
            'author': details.find(text=re.compile("Author")).next_sibling.get_text(strip=True),
            'artist': details.find(text=re.compile("Artist")).next_sibling.get_text(strip=True),
            'rating': self.parsed_html.find('div',{'class': 'rating'}).find('div',{'class': 'num'}).get_text(strip=True),
            'chapter': ms.getMangaChapterDetails(chapters),
        }
        return manga
    
    def getChapter(self):
        if self.check404 == True:
            return False
        image = mangastream(self.parsed_html).getChapter() 

        return image