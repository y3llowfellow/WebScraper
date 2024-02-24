from PriceTracker import Scraper
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import Flask, render_template
import threading
from datetime import datetime
import numpy as np
import pandas as pd

watchlist = [
    "https://www.amazon.com/Apple-Generation-Cancelling-Transparency-Personalized/dp/B0CHWRXH8B/ref=sr_1_4?crid=2328EFCIMKH5J&keywords=airpods&qid=1706060481&sprefix=airpo%2Caps%2C152&sr=8-4&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0",
    "https://www.amazon.com/Mighty-Patch-Hydrocolloid-Absorbing-count/dp/B074PVTPBW/?_encoding=UTF8&pd_rd_w=uYSSW&content-id=amzn1.sym.64be5821-f651-4b0b-8dd3-4f9b884f10e5&pf_rd_p=64be5821-f651-4b0b-8dd3-4f9b884f10e5&pf_rd_r=WHK1T4SQ8QGKJ0K6TFVX&pd_rd_wg=g2948&pd_rd_r=a0263006-aa76-45f1-bf1e-b0b4528ee417&ref_=pd_gw_crs_zg_bs_3760911"
    ]
sc = Scraper(watchlist[1])

name = sc.getTitle()
print(sc.getPrice())

w, h = 2, 0
prices = [[0 for x in range(w)] for y in range(h)]


def updateTables():
    threading.Timer(15, updateTables).start()
    prices.append([datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), sc.getPrice()])
    df = pd.DataFrame(prices, ["Time", "Price"])
    html = df.to_html()
    print(html)
    # print(np.matrix(prices))
    # print()


updateTables()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("C:\\Users\\colin\\PycharmProjects\\WebScraper\\prices.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
