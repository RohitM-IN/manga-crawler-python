from utils.crawler import crawler
from flask import jsonify
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

class madara:
    def __init__(self,parsed_html):
        self.parsed_html = parsed_html

    def getList(self):
        data = []

        elements = self.parsed_html.find_all('div',{"class" : 'manga'})

        for items in elements:
            title = items.find('div',{'class':'post-title'}).get_text(strip=True)
            image = items.find('img').get('data-src') if items.find('img') else None
            url = items.find('div',{'class':'post-title'}).find('a').get('href')
            rating = items.find('span',{'class': 'score'}).get_text(strip=True)
            chapters = items.find_all('div',{'class': 'chapter-item'})

            chapter = []

            for item in chapters:
                ch = {
                    'title': item.find('span',{'class':'chapter'}).get_text(strip=True),
                    'url': item.find('a').get('href'),
                    'date': item.find('span',{'class': 'post-on'}).get_text(strip=True)
                }
                chapter.append(ch)

            manga = {
                'title': title,
                'image': image,
                'chapter': chapter,
                'rating': rating,
                'url': url
            }

            data.append(manga)

        return data
    
    def getChapter(self):
        el = self.parsed_html.find('div',{'class': 'reading-content'})

        image = []

        for element in el.find_all('img'):
            image.append(element.get('data-src').strip())

        return image
