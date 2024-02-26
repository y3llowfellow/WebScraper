import datetime
from Scraper import Scraper
import warnings
warnings.simplefilter(action='ignore', category=DeprecationWarning)
from flask import Flask, render_template, render_template_string
import pandas as pd
import logging
#Disble unnecessary console logs w/ logging import
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
import argparse

#Prompt users using the command line
parser = argparse.ArgumentParser(description='Track items and send emails')
parser.add_argument('num_items', type=int, help='Number of items to track')
parser.add_argument('interval_ms', type=int, help='Milliseconds between checks')
parser.add_argument('email', type=str, help='Email address to send notifications')
args = parser.parse_args()

number = args.num_items
scrapers = []
email = args.email
RefreshRate = args.interval_ms
#Populate watchlist with user entered links
for i in range(1, number+1):
    link = input("Enter item " + str(i) + " url: " )
    sc = Scraper(link, email)
    scrapers.append(sc)
#Begin flask webpage
app = Flask(__name__)

#Record the last time the table was updated to ensure that the timer is working properly
lastTime = datetime.datetime(2024, 2, 20, 11, 11, 11)

#Record the last updated table, in case if updateTables() prematurely updates
previous = " "

#Populate table w/ prices
@app.route('/data')
def updateTables():
    # Beginning of HTML file template
    html_head = """
    <!DOCTYPE html>
    <html lang = "en">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <h1>Price Tracker</h1>
        </head>
        <body>
        <script type="text/javascript" src="http://code.jquery.com/jquery-1.8.0.min.js"></script>
            <script type="text/javascript">
                function updater() {
                  $.get('/data', function(data) {
                    $('*').html(data);  // update page with new data
                  });
                };
                setInterval(updater,""" + str(RefreshRate) + """);  // run `updater()` every 1000ms (1s)
            </script>
    """
    #End of html file template
    html_end = """
        </body>
    </html>
    """
    global lastTime
    #Check if table needs to be updated based on the refresh rate
    if (datetime.datetime.now() - lastTime).total_seconds() > (int(RefreshRate)/1000-1):
        lastTime = datetime.datetime.now()
        #Loop through each product
        for j in range(0, number):
            # create table for to display prices and time using scraper objects
            table = scrapers[j].getTable()
            df = pd.DataFrame(table)
            htmlChart = df.to_html(header=False, index=False)
            #Add product name as a title
            ProductName = "<h2>" + scrapers[j].getTitle() + "<h2>\n"
            #Combine all HTML files together
            html_head += ProductName + htmlChart
            global previous
            previous = html_head + html_end
    return previous
#Render Flask webpage with HTML file from the updateTables() function
@app.route('/')
def home():
    return render_template_string(updateTables())
#Launches Flask website
if __name__ == '__main__':
    #Prints website for user access
    print("Go to http://127.0.0.1:5000/ on Google for live updates!")
    app.run()