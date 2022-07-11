from utils.cleaners.common.mangastream import mangastream
from utils.crawler import crawler
from utils.utils import chapterFixer
from bs4 import BeautifulSoup

class flame:
    def __init__(self, url):
        self.url = url
        self.html = crawler(self.url).get()
        self.parsed_html = BeautifulSoup(self.html,'html.parser')
        self.notFound = self.check404()
    
    def check404(self):
        if "Page not found" in self.parsed_html.title.get_text():
            return True
        return False
    
    def getList(self):
        data = mangastream(self.parsed_html.find('div',{"class" : 'listupd'})).getList()
        return data
    
    def getManga(self):
        def filterList(i):
            if i == '\n' or i == '\xa0' or i.strip() == '':
                return False
            return True
        if self.notFound == True:
            return False

        details = self.parsed_html.find('div',{'class': 'first-half'})
        chapters =  self.parsed_html.find('div',{'class':'second-half'}).find('div',{'class': 'eplister'}).find_all('li')

        md = mangastream(self.parsed_html)
        chapter = md.getMangaChapterDetails(chapters)
        genre = md.getMangaGenreDetails()
        extra = self.parsed_html.find('div',{'class': 'tsinfo'}).find_all('div',{'class':'imptdt'})

        info = []
        for element in extra:
            if element.find('h1') is None:
                continue
            key = element.find('h1').get_text(strip=True)
            value = element.find('i').get_text(strip=True)
            el = {
             key : value
            }
            info.append(el)
    
        about = list(filter(filterList,details.find('div',{'class': 'entry-content'}).find_all(text=True))) 
        original = None
        if about[-3] == "Additional Information":
            original = details.find('div',{'class': 'entry-content'}).find('u').find('a').get('href')
            about = about[:-3]
        about = ' \n'.join(about)
        
        manga = {
            'title': details.find('div',{'class':'titles'}).get_text(strip=True),
            'alt-title' : list(details.find('div',{'class':'desktop-titles'}).get_text(strip=True).split('|')),
            'image': details.find('div',{'class': 'thumb-half'}).find('img').get('src'),
            'genre': genre,
            'chapters': chapter,
            'details': about,
            'original': original,
            'status': details.find('div',{'class': 'status'}).get_text(strip=True),
            'rating': details.find('div',{'class': 'numscore'}).get_text(strip=True),
            'extra': info
        }
        return manga
    
    def getChapter(self):
        if self.check404 == True:
            return False
        images = self.parsed_html.find("div",{'id': 'readerarea'}).find_all('img')
        image = mangastream(None).getChapter(images) 
        return image