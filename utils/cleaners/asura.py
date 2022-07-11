import re
from utils.crawler import crawler
from utils.cleaners.common.mangastream import mangastream
from bs4 import BeautifulSoup

class asura:
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

        details = self.parsed_html.find('div',{'class': 'thumbook'})
        details_2 = self.parsed_html.find('div',{'class': 'infox'})

        author = artist = rating = status = Mtype = "-"
        if details_2.find('b',text=re.compile("Author")):
            author = details_2.find('b',text=re.compile("Author")).parent.find('span').get_text(strip=True)
        if details_2.find('b',text=re.compile("Artist")):
            artist = details_2.find('b',text=re.compile("Artist")).parent.find('span').get_text(strip=True)
        if details.find('div',{'class': 'rating'}):
            rating = details.find('div',{'class': 'rating'}).find('div',{'class': 'num'}).get_text(strip=True)
        if details.find(text=re.compile("Status")):
            status = details.find(text=re.compile("Status")).next_sibling.get_text(strip=True)
        if details.find(text=re.compile("Type")):
            Mtype = details.find(text=re.compile("Type")).next_sibling.get_text(strip=True)

        manga = {
            'title': ms.getMangaDetails(('h1',{'class': 'entry-title'}),"infox").get_text(strip=True),
            'image': ms.getMangaDetails(('div',{'class': 'thumb'}),"thumbook").find('img').get('src'),
            'description': ms.getMangaDetails(('div',{'class': 'entry-content'}),"infox").get_text(strip=True),
            'genre': ms.getMangaGenreDetails(('span',{'class': 'mgen'})),
            'type': Mtype,
            'status': status,
            'author': author,
            'artist': artist,
            'rating': rating,
            'chapter': ms.getMangaChapterDetails(chapters),
        }

        return manga
    
    def getChapter(self):
        if self.check404 == True:
            return False
        images = self.parsed_html.find("div",{'id': 'readerarea'}).find_all('img')
        image = mangastream(None).getChapter(images) 

        return image