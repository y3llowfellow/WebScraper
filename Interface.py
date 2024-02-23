from PriceTracker import Scraper
from urllib.request import urlopen
from bs4 import BeautifulSoup

watchlist = ["https://www.amazon.com/Apple-Generation-Cancelling-Transparency-Personalized/dp/B0CHWRXH8B/ref=sr_1_4?crid=2328EFCIMKH5J&keywords=airpods&qid=1706060481&sprefix=airpo%2Caps%2C152&sr=8-4&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0"]
sc = Scraper(watchlist)

# page = urlopen(watchlist[0])
# html_bytes = page.read()
# html = html_bytes.decode("utf8")
# print(html)
