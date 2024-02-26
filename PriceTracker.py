import smtplib
from datetime import datetime
from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup
from smtplib import SMTP


class Scraper:
    def __init__(self, link, email):
        self.price = []
        self.time = []

        self.table = [[0 for x in range(2)] for y in range(0)]
        self.table.append(["Times", "Prices"])
        self.title = None
        self.link = link
        self.email = email

    def populate(self):
        page = urlopen(self.link)
        html_bytes = page.read()
        html = html_bytes.decode("utf8")
        soup = BeautifulSoup(html, "html.parser")
        # image = soup.find('div',{'id':'imageBlock'}).text.strip()

        lastPrice = self.table[len(self.table) - 1][1]
        time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        newPrice = soup.find('span', {
            'class': 'a-offscreen'}).text.strip()
        self.table.append([time, newPrice])

        self.title = soup.find('h1', {'id': 'title'}).text.strip()

        if (lastPrice != newPrice):
            self.sendMail(lastPrice, newPrice)

    def getTable(self):
        self.populate()
        return self.table

    def getTitle(self):
        return self.title

    def sendMail(self, oldPrice, newPrice):
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("pricealerts611@gmail.com", "atju krdm dwwl mqsf")
        server.sendmail("pricealerts611@gmail.com", self.email,
                        "The price of " + self.title +" has changed from " + str(oldPrice) + " to " + str(newPrice))
