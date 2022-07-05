from utils.crawler import crawler
from flask import jsonify
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

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
            image = el.find('img').get('src')
            url = el.find('a').get('href')
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
                'url': element.find('a').get('href'),
                'date': element.find('span',{'class': 'chapterdate'}).get_text(strip=True)
            }
            chapter.append(ch)
        
        genre = []

        for element in el.find('span',{'class': 'mgen'}).find_all('a'):
            genre.append(element.get_text(strip=True))

        manga = {
            'title': details.select_one('h1.entry-title').get_text(strip=True),
            'image': el.find('img').get('src'),
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
            image.append(element.get('src'))

        return image


class reaper:
    def __init__(self, url):
        self.url = url

    def getList(self,count,perPage):
        data = []

        html = crawler(self.url).post(self.getContent(count,perPage),self.getHeader())
        parsed_html = BeautifulSoup(html,'html.parser')

        # print(parsed_html.prettify())

        elements = parsed_html.find_all('div',{"class" : 'manga'})

        for items in elements:

            title = items.find('div',{'class':'post-title'}).get_text(strip=True)
            image = items.find('img').get('data-src')
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

    def getManga(self):

        html = crawler(self.url).get()

        parsed_html = BeautifulSoup(html,'html.parser')

        chapters =  parsed_html.find('div',{'class': 'c-page-content'}).find_all('li')

        details = parsed_html.find('div',{'class': 'profile-manga'})

        # print(el.find('div',{'class': 'infox'}).prettify())

        chapter = []

        for element in chapters:
            ch = {
                'title': element.find('p').get_text(strip=True),
                'url': element.find('a').get('href'),
                'index': element.find('p').get_text(strip=True).split('-')[0].split(' ')[1],
                'date': element.find('span').get_text(strip=True)
            }
            chapter.append(ch)
        
        genre = []

        for element in details.find('div',{'class': 'genres-content'}).find_all('a'):
            genre.append(element.get_text(strip=True))
        
        author = []
        for element in details.find('div',{'class': 'author-content'}).find_all('a'):
            author.append(element.get_text(strip=True))
        
        manga = {
            'title': details.find('div',{'class':'post-title'}).find('h1').get_text(strip=True),
            'image': details.find('div',{'class': 'summary_image'}).find('img').get('data-src'),
            'description': details.find('div',{'class': 'description-summary'}).find('p').get_text(strip=True),
            'genre': genre,
            'type': details.find('div',{'class': 'post-content'}).select_one('div:nth-child(8) > div.summary-content').get_text(strip=True),
            'chapter': chapter,
            'author' : author
        }

        return manga

    def getChapter(self):

        html = crawler(self.url).get()

        parsed_html = BeautifulSoup(html,'html.parser')

        el = parsed_html.find('div',{'class': 'reading-content'})

        image = []

        for element in el.find_all('img'):
            image.append(element.get('data-src').strip())

        return image

    def getContent(self,page,perPage):
        return "action=madara_load_more&page={0}&template=madara-core%2Fcontent%2Fcontent-archive&vars%5Borderby%5D=meta_value_num&vars%5Bpaged%5D=1&vars%5Btimerange%5D=&vars%5Bposts_per_page%5D={1}&vars%5Btax_query%5D%5Brelation%5D=OR&vars%5Bmeta_query%5D%5B0%5D%5B0%5D%5Bkey%5D=_wp_manga_chapter_type&vars%5Bmeta_query%5D%5B0%5D%5B0%5D%5Bvalue%5D=manga&vars%5Bmeta_query%5D%5B0%5D%5Brelation%5D=AND&vars%5Bmeta_query%5D%5Brelation%5D=OR&vars%5Bpost_type%5D=wp-manga&vars%5Bpost_status%5D=publish&vars%5Bmeta_key%5D=_latest_update&vars%5Border%5D=desc&vars%5Bsidebar%5D=full&vars%5Bmanga_archives_item_layout%5D=big_thumbnail".format(page,perPage)

    def getHeader(self):
        return {
            'content-type' : 'application/x-www-form-urlencoded; charset=UTF-8',
            'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding' : 'gzip, deflate, br',
            'accept-language' : 'en-US,en;q=0.9',
            'cache-control' : 'max-age=0',
            'referer' : 'https://reaperscans.com'
        }