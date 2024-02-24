from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, link):
        self.price = None
        self.title = None
        self.link = link
        self.populate()

    def populate(self):
        page = urlopen(self.link)
        html_bytes = page.read()
        html = html_bytes.decode("utf8")
        soup = BeautifulSoup(html, "html.parser")
        # image = soup.find('div',{'id':'imageBlock'}).text.strip()
        self.title, self.price = soup.find('h1', {'id': 'title'}).text.strip(), soup.find('span', {
            'class': 'a-offscreen'}).text.strip()

    def getPrice(self):
        self.populate()
        return self.price

    def getTitle(self):
        self.populate()
        return self.title
