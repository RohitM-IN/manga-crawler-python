from utils.crawler import crawler
from utils.cleaners.common.madara import madara
from bs4 import BeautifulSoup


class reaper:
    def __init__(self, url):
        self.url = url

    def getList(self,count,perPage):
        data = []
        html = crawler(self.url).post(self.getContent(count,perPage),self.getHeader())
        parsed_html = BeautifulSoup(html,'html.parser')

        data = madara(parsed_html).getList()
        return data

    def getManga(self):
        html = crawler(self.url).get()
        parsed_html = BeautifulSoup(html,'html.parser')

        details = parsed_html.find('div',{'class': 'profile-manga'})

        md = madara(parsed_html)

        chapter = md.getChapterDetails('c-page-content')
        
        genre = md.getDetails('genres-content','div')
        
        author = md.getDetails('author-content','div')
        
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

        data = madara(parsed_html).getChapter()
        return data

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
