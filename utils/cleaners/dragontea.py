from utils.crawler import crawler
from utils.cleaners.madara import madara as md
from utils.utils import chapterFixer
from flask import jsonify
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

class dragontea:
    def __init__(self, url):
        self.url = url

    def getList(self,count,perPage):
        html = crawler(self.url).post(self.getContent(count,perPage),self.getHeader())
        parsed_html = BeautifulSoup(html,'html.parser')

        data = md(parsed_html).getList()

        return data

    def getManga(self):
        html = crawler(self.url).get()
        parsed_html = BeautifulSoup(html,'html.parser')

        chapters_raw = crawler(self.url + "ajax/chapters/").post(None,None)
        chapters_parsed = BeautifulSoup(chapters_raw,'html.parser')
        chapters =  chapters_parsed.find('div',{'class': 'listing-chapters_wrap'}).find_all('li')

        details = parsed_html.find('div',{'class': 'summary_content'})

        chapter = []

        for element in chapters:
            ch = {
                'title': chapterFixer(element.find('a').get_text(strip=True)),
                'url': element.find('a').get('href'),
                'date': element.find('span').get_text(strip=True)
            }
            chapter.append(ch)
        
        genre = []

        for element in details.find('div',{'class': 'genres-content'}).find_all('a'):
            genre.append(element.get_text(strip=True))
        
        author = []
        if details.find('div',{'class': 'author-content'}):
            for element in details.find('div',{'class': 'author-content'}).find_all('a'):
                author.append(element.get_text(strip=True))
        
        Manga_Type = "" 
        for el in details.find('div',{'class': 'post-content'}).find_all('div',{'class':'post-content_item'}):
            if el.find('div',{'class':'summary-heading'}).get_text(strip=True) == 'Type':
                Manga_Type = el.find('div',{'class':'summary-content'}).get_text(strip=True)

        status = ""
        if details.find('div',{'class': 'post-status'}):
            for el in details.find('div',{'class': 'post-status'}).find_all('div',{'class': 'post-content_item'}):
                if el.find('div',{'class':'summary-heading'}).get_text(strip=True) == 'Status':
                    status = el.find('div',{'class':'summary-content'}).get_text(strip=True)
        
        manga = {
            'title': parsed_html.find('div',{'class':'post-title'}).find('h1').get_text(strip=True),
            'image': parsed_html.find('div',{'class': 'summary_image'}).find('img').get('data-src'),
            'description': parsed_html.find('div',{'class': 'description-summary'}).find('p').get_text(strip=True),
            'genre': genre,
            'type': Manga_Type,
            'chapter': chapter,
            'author' : author,
            'status' : status
        }

        return manga
    
    def getChapter(self):
        html = crawler(self.url).get()
        parsed_html = BeautifulSoup(html,'html.parser')

        data = md(parsed_html).getChapter()

        return data
    
    def getContent(self,count,perPage):
        data = "action=madara_load_more&page={0}&template=madara-core%2Fcontent%2Fcontent-archive&vars%5Bwp-manga-genre%5D=comics&vars%5Berror%5D=&vars%5Bm%5D=&vars%5Bp%5D=0&vars%5Bpost_parent%5D=&vars%5Bsubpost%5D=&vars%5Bsubpost_id%5D=&vars%5Battachment%5D=&vars%5Battachment_id%5D=0&vars%5Bname%5D=&vars%5Bpagename%5D=&vars%5Bpage_id%5D=0&vars%5Bsecond%5D=&vars%5Bminute%5D=&vars%5Bhour%5D=&vars%5Bday%5D=0&vars%5Bmonthnum%5D=0&vars%5Byear%5D=0&vars%5Bw%5D=0&vars%5Bcategory_name%5D=&vars%5Btag%5D=&vars%5Bcat%5D=&vars%5Btag_id%5D=&vars%5Bauthor%5D=&vars%5Bauthor_name%5D=&vars%5Bfeed%5D=&vars%5Btb%5D=&vars%5Bpaged%5D=1&vars%5Bmeta_key%5D=_latest_update&vars%5Bmeta_value%5D=&vars%5Bpreview%5D=&vars%5Bs%5D=&vars%5Bsentence%5D=&vars%5Btitle%5D=&vars%5Bfields%5D=&vars%5Bmenu_order%5D=&vars%5Bembed%5D=&vars%5Bignore_sticky_posts%5D=false&vars%5Bsuppress_filters%5D=false&vars%5Bcache_results%5D=true&vars%5Bupdate_post_term_cache%5D=true&vars%5Blazy_load_term_meta%5D=true&vars%5Bupdate_post_meta_cache%5D=true&vars%5Bpost_type%5D=wp-manga&vars%5Bposts_per_page%5D={1}&vars%5Bnopaging%5D=false&vars%5Bcomments_per_page%5D=50&vars%5Bno_found_rows%5D=false&vars%5Btaxonomy%5D=wp-manga-genre&vars%5Bterm%5D=comics&vars%5Border%5D=desc&vars%5Borderby%5D=meta_value_num&vars%5Btemplate%5D=archive&vars%5Bsidebar%5D=right&vars%5Bpost_status%5D=publish&vars%5Bmeta_query%5D%5B0%5D%5Bwp-manga-genre%5D=comics&vars%5Bmeta_query%5D%5B0%5D%5Berror%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bm%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bp%5D=0&vars%5Bmeta_query%5D%5B0%5D%5Bpost_parent%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bsubpost%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bsubpost_id%5D=&vars%5Bmeta_query%5D%5B0%5D%5Battachment%5D=&vars%5Bmeta_query%5D%5B0%5D%5Battachment_id%5D=0&vars%5Bmeta_query%5D%5B0%5D%5Bname%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bpagename%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bpage_id%5D=0&vars%5Bmeta_query%5D%5B0%5D%5Bsecond%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bminute%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bhour%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bday%5D=0&vars%5Bmeta_query%5D%5B0%5D%5Bmonthnum%5D=0&vars%5Bmeta_query%5D%5B0%5D%5Byear%5D=0&vars%5Bmeta_query%5D%5B0%5D%5Bw%5D=0&vars%5Bmeta_query%5D%5B0%5D%5Bcategory_name%5D=&vars%5Bmeta_query%5D%5B0%5D%5Btag%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bcat%5D=&vars%5Bmeta_query%5D%5B0%5D%5Btag_id%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bauthor%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bauthor_name%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bfeed%5D=&vars%5Bmeta_query%5D%5B0%5D%5Btb%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bpaged%5D=1&vars%5Bmeta_query%5D%5B0%5D%5Bmeta_key%5D=_latest_update&vars%5Bmeta_query%5D%5B0%5D%5Bmeta_value%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bpreview%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bs%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bsentence%5D=&vars%5Bmeta_query%5D%5B0%5D%5Btitle%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bfields%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bmenu_order%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bembed%5D=&vars%5Bmeta_query%5D%5B0%5D%5Bignore_sticky_posts%5D=false&vars%5Bmeta_query%5D%5B0%5D%5Bsuppress_filters%5D=false&vars%5Bmeta_query%5D%5B0%5D%5Bcache_results%5D=true&vars%5Bmeta_query%5D%5B0%5D%5Bupdate_post_term_cache%5D=true&vars%5Bmeta_query%5D%5B0%5D%5Blazy_load_term_meta%5D=true&vars%5Bmeta_query%5D%5B0%5D%5Bupdate_post_meta_cache%5D=true&vars%5Bmeta_query%5D%5B0%5D%5Bpost_type%5D=wp-manga&vars%5Bmeta_query%5D%5B0%5D%5Bposts_per_page%5D=12&vars%5Bmeta_query%5D%5B0%5D%5Bnopaging%5D=false&vars%5Bmeta_query%5D%5B0%5D%5Bcomments_per_page%5D=50&vars%5Bmeta_query%5D%5B0%5D%5Bno_found_rows%5D=false&vars%5Bmeta_query%5D%5B0%5D%5Btaxonomy%5D=wp-manga-genre&vars%5Bmeta_query%5D%5B0%5D%5Bterm%5D=comics&vars%5Bmeta_query%5D%5B0%5D%5Border%5D=desc&vars%5Bmeta_query%5D%5B0%5D%5Borderby%5D=meta_value_num&vars%5Bmeta_query%5D%5B0%5D%5Btemplate%5D=archive&vars%5Bmeta_query%5D%5B0%5D%5Bsidebar%5D=right&vars%5Bmeta_query%5D%5B0%5D%5Bpost_status%5D=publish&vars%5Bmeta_query%5D%5Brelation%5D=AND".format(count,perPage)

        return data
    
    def getHeader(self):
        return {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'referer': 'https://dragontea.ink/novel-genre/comics/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }

    