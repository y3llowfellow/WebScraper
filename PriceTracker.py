from urllib.request import urlopen
from bs4 import BeautifulSoup
class Scraper:
    def __init__(self, watchList):
        self.watchList = watchList
        self.populate()

    def populate(self):
        titles = []
        for i in self.watchList:
            page = urlopen(i)
            html_bytes = page.read()
            html = html_bytes.decode("utf8")
            soup= BeautifulSoup(html, "html.parser")
            title = soup.find('h1', {'id': 'title'}).text.strip()
            price = soup.find('span',{'class':'a-offscreen'}).text.strip()
            print(price)






