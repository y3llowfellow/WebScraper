from PriceTracker import Scraper
import warnings
warnings.simplefilter(action='ignore', category=DeprecationWarning)

from bs4 import BeautifulSoup
from flask import Flask, render_template, render_template_string
import threading
from datetime import datetime
import numpy as np
import pandas as pd
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler


#prompt users
number = int(input("How many items would you like to track?"))
scrapers = []

#populate watchlist with user entered links
for i in range(1, number+1):
    link = input("Enter item " + str(i) + " url: " )
    sc = Scraper(link)
    scrapers.append(sc)

#populate table w/ prices
def updateTables():
    # beginning of Html file template
    html_head = """
    <!DOCTYPE html>
    <html lang = "en">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <h1>Price Tracker</h1>
        </head>
        <body>
    """
    # end of html file template
    html_end = """
        </body>
    </html>
    """

    for j in range(0, number):
        # create table for to display prices and time
        table = scrapers[j].getTable()
        df = pd.DataFrame(table)
        htmlChart = df.to_html(header=False, index=False)
        ProductName = "<h2>" + scrapers[j].getTitle() + "<h2>\n"
        html_head += ProductName + htmlChart
    return html_head + html_end



app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string(updateTables())

if __name__ == '__main__':
    app.run()
