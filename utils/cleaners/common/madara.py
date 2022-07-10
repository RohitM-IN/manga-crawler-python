from utils.utils import chapterFixer

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
                    'title': chapterFixer(item.find('span',{'class':'chapter'}).get_text(strip=True)),
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
    
    def getChapter(self,chapterClass = 'reading-content'):
        el = self.parsed_html.find('div',{'class': chapterClass})

        image = []

        for element in el.find_all('img'):
            image.append(element.get('data-src').strip())

        return image
    
    def getChapterDetails(self,chaptersClass = 'listing-chapters_wrap',chaptersTag = 'div'):
        chapter = []
        chapters =  self.parsed_html.find(chaptersTag,{'class': chaptersClass})

        for element in chapters.find_all('li'):
            ch = {
                'title': chapterFixer(element.find('p').get_text(strip=True)),
                'url': element.find('a').get('href'),
                'date': element.find('span').get_text(strip=True)
            }
            chapter.append(ch)
        
        return chapter
    
    def getDetails(self,detailsClass = 'genres-content',detailsTag = 'div'):
        details = []
        for element in self.parsed_html.find(detailsTag,{'class': detailsClass}).find_all('a'):
            details.append(element.get_text(strip=True))
        return details

