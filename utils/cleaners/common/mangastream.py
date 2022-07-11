from utils.utils import chapterFixer, fixUrl

class mangastream:
    def __init__(self, parsed_html):
        self.parsed_html = parsed_html


    def getList(self, chapterClass = 'bs'):
        data = []

        elements = self.parsed_html.find_all('div',{"class" : chapterClass})

        for el in elements:
            title = el.find('div',{'class': 'tt'}).get_text(strip=True)
            image = el.find('img').get('src')
            url = el.find('a').get('href')
            chapter = el.find('div',{'class': 'epxs'}).get_text(strip=True) if el.find('div',{'class': 'epxs'}) else None
            rating = el.find('div',{'class': 'numscore'}).get_text(strip=True) if el.find('div',{'class': 'numscore'}) else None
            status = el.find('div',{'class': 'status'}).get_text(strip=True) if el.find('div',{'class': 'status'}) else None
            
            manga = {
                'title': title,
                'image': fixUrl(str(image)),
                'status': status,
                'rating': rating,
                'url': fixUrl(str(url)),
                'chapter': chapter,
                'status': status
            }
            data.append(manga)

            manga = {
                'title': title,
                'image': image,
                'chapter': chapter,
                'rating': rating,
                'url': url
            }

            data.append(manga)

        return data
    
    def getMangaDetails(self,ClassDiv = ('h1',{'class': 'entry-title'}),classFind = 'infox'):
        details = self.parsed_html.find('div',{'class': classFind})
        return details.find(ClassDiv)
    def getMangaChapterDetails(self,chapters):
        chapter = []
        for el in chapters:
            ch = {
                'title': chapterFixer(el.find('span',{'class': 'chapternum'}).get_text(strip=True)),
                'url': el.find('a').get('href'),
                'date': el.find('span',{'class': 'chapterdate'}).get_text(strip=True)
            }
            chapter.append(ch)
        
        return chapter

    def getMangaGenreDetails(self,ClassDiv = ('span',{'class': 'mgen'})):
        genre = []

        for element in self.parsed_html.find(ClassDiv).parent.find_all('a'):
            genre.append(element.get_text(strip=True))
        return genre
    
    def getChapter(self,images):
        image = []

        for element in images:
            if element.get('style') and "display: none" in element.get('style'):
                continue
            image.append(element.get('src'))
        return image