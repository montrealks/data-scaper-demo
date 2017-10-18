__author__ = "Kris"
from bs4 import BeautifulSoup
import requests
from src.example import GuardianHomePage

class GetTheGaurdianData():
    HOME_PAGE_DATA = None
    HOME_PAGE_DATA_FORMATTED = None
    LOCAL_LOAD = False
    FORMATTED_FOR_CSV = None
    
    @staticmethod
    def load_home_page(ghp=None):
        if not GetTheGaurdianData.LOCAL_LOAD:
            r = requests.get("https://www.theguardian.com/")
            soup = BeautifulSoup(r.text, "html5lib")
            GetTheGaurdianData.HOME_PAGE_DATA = soup
            # l = soup.findAll('div', {'class': 'fc-item__container'})
        else:
            soup = BeautifulSoup(GuardianHomePage, "html5lib")
            GetTheGaurdianData.HOME_PAGE_DATA = soup
        print("succesfully retrieved the home page")

    
    @staticmethod
    def load_headlines(quantity_of_articles='all'):
        soup = GetTheGaurdianData.HOME_PAGE_DATA
        l = soup.findAll("div", class_="fc-item__container")
        headlines = []
        
        if quantity_of_articles == 'all':
            start = 0
            finish = len(l)
        elif quantity_of_articles == 10:
            start = 6
            finish = 8
        
        for item in l[start:finish]:
            headline = {}
            headline['headline_title'] = item.find('span', {"class": "u-faux-block-link__cta fc-item__headline"}).text
            try:
                headline['headline_body'] = item.find('div', {"class": "fc-item__standfirst"}).text 
            except:
                headline['headline_body'] = 'No body on front page'
                
            try:
                headline['headline_kicker'] = item.find('span', {'class': 'fc-item__kicker'}).text
            except:
                headline['headline_kicker'] = 'None found'
                
            headline['headline_link'] = item.find('a', {'class': "fc-item__link"}).get('href')
            
            
            headlines.append(headline)
            
        GetTheGaurdianData.HOME_PAGE_DATA_FORMATTED = headlines
        return headlines
        
        
        
    @staticmethod
    def get_per_page_details(position):
        data_with_details = []
        author_names = None
        
        # for article in GetTheGaurdianData.HOME_PAGE_DATA_FORMATTED:
        article = GetTheGaurdianData.HOME_PAGE_DATA_FORMATTED[position]
        meta_data = {}
        meta_data['title'] = article['headline_title']
        # Load the article page
        r = requests.get(article['headline_link'])
        soup = BeautifulSoup(r.text, "html5lib")
        
        # create an object out of the meta content data
        meta_content = soup.find('div', {'class': "content__meta-container"})
        
        if meta_content == None:
            print("this article doesn't have regular meta content")
            meta_data = {
                    'authors': 'None Found',
                    'keywords': 'None Found',
                    'date': 'None Found'
                    }
            data_with_details.append(meta_data)
            return data_with_details
            
        # Get the author(s)
        authors = meta_content.findAll('span', {'itemprop': 'name'})
        
        if len(authors) > 0:
            meta_data['authors'] = authors[0].text
            if len(authors) > 1:
                for author in authors[1:]:
                    meta_data['authors'] += ', ' + author.text
        else:
            meta_data['authors'] = 'No Authors Found'
            print("Authors: ", meta_data['authors'])
                
        # Get the date
        
        date_string = soup.find('time', {'class': 'content__dateline-wpd'}).text
        
        date_time_string = soup.find('span', {'class': 'content__dateline-time'}).text
        meta_data['date'] = date_string + ' ' + date_time_string
        print(meta_data['date'])
        
        # get meta tags
        keywords = soup.findAll('li', {'class': 'submeta__link-item'})
        meta_data['keywords'] = ''
        for keyword in keywords:
            text = keyword.find('a').text
            link = keyword.find('a').get('href')
            meta_data['keywords'] += "<a href='{}'>{}</a> ".format(link, text)
        
        data_with_details.append(meta_data) 
        print(data_with_details)
        return data_with_details
        
        
        
            
                
        # return data_with_details
        

# g = GetTheGaurdianData()
# g.load_home_page(ghp)
# g.load_headlines()