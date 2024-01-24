import smtplib
import pandas as pd
import requests
from bs4 import BeautifulSoup
from price_parser import Price


watchList = ['https://www.amazon.com/Apple-Generation-Cancelling-Transparency-Personalized/dp/B0CHWRXH8B/ref=sr_1_4?crid=2328EFCIMKH5J&keywords=airpods&qid=1706060481&sprefix=airpo%2Caps%2C152&sr=8-4&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0']

def getPrice(link):
    try:
        soup = BeautifulSoup(html, "lxml")
        el = soup.select_one(".price_color")
        price = Price.fromstring(el.text)
        return price.amount_float