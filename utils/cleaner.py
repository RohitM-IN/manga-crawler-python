from utils.crawler import crawler
from flask import jsonify
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def response(data,status=200,message="success"):

    return jsonify({'status': status , 'data' : data, 'message' : message})

def make_error(status_code, message, error):
    response = jsonify({
        'status': status_code,
        'error': {
            'message': message,
            'type': error
        }
    })
    response.status_code = status_code
    return response

class asura:
    def __init__(self, url):
        self.url = url
        self.html = crawler(self.url).get()
        self.parsed_html = BeautifulSoup(self.html,'html.parser')

    def getList(self):
        data = []

        elements = self.parsed_html.find_all('div',{"class" : 'bs'})

        for el in elements:
            title = el.find('div',{'class': 'tt'}).get_text(strip=True)
            image = el.find('img')['src']
            url = el.find('a')['href']
            chapter = el.find('div',{'class': 'epxs'}).get_text(strip=True)
            rating = el.find('div',{'class': 'numscore'}).get_text(strip=True)

            manga = {
                'title': title,
                'image': image,
                'chapter': chapter,
                'rating': rating,
                'url': url
            }

            data.append(manga)

        return data

    def getManga(self):
        el = self.parsed_html.find('div',{'class': 'postbody'})

        chapters =  el.select('#chapterlist > ul > li')

        details = el.find('div',{'class': 'infox'})

        # print(el.find('div',{'class': 'infox'}).prettify())

        chapter = []

        for element in chapters:
            ch = {
                'title': element.find('span',{'class': 'chapternum'}).get_text(strip=True),
                'url': element.find('a')['href'],
                'date': element.find('span',{'class': 'chapterdate'}).get_text(strip=True)
            }
            chapter.append(ch)
        
        genre = []

        for element in el.find('span',{'class': 'mgen'}).find_all('a'):
            genre.append(element.get_text(strip=True))

        manga = {
            'title': details.select_one('h1.entry-title').get_text(strip=True),
            'image': el.find('img')['src'],
            'description': el.find('div',{'class': 'entry-content'}).get_text(strip=True),
            'genre': genre,
            'type': el.find('div',{'class': 'tsinfo'}).select_one('div.imptdt:nth-of-type(2) > a').get_text(strip=True),
            'chapter': chapter,
        }

        return manga
    
    def getChapter(self):
        el = self.parsed_html.find('div',{'id': 'readerarea'})

        image = []

        for element in el.find_all('img')[1:-1]:
            image.append(element['src'])

        return image
