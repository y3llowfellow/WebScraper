import datetime

from PriceTracker import Scraper
import warnings
warnings.simplefilter(action='ignore', category=DeprecationWarning)

from flask import Flask, render_template, render_template_string
import pandas as pd



#prompt users
number = int(input("How many items would you like to track?"))
scrapers = []
email = input("what is your email address?")
RefreshRate = input("How often would you like to update the price table? Enter time in ms: ")
#populate watchlist with user entered links
for i in range(1, number+1):
    link = input("Enter item " + str(i) + " url: " )
    sc = Scraper(link, email)
    scrapers.append(sc)


finalHtml = ""

app = Flask(__name__)

lastTime = datetime.datetime(2024, 2, 20, 11, 11, 11)
previous = " "
#populate table w/ prices
@app.route('/data')
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
        <script type="text/javascript" src="http://code.jquery.com/jquery-1.8.0.min.js"></script>
            <script type="text/javascript">
                function updater() {
                  $.get('/data', function(data) {
                    $('*').html(data);  // update page with new data
                  });
                };
                setInterval(updater,""" + RefreshRate + """);  // run `updater()` every 1000ms (1s)
            </script>
    """
    # end of html file template
    html_end = """
        </body>
    </html>
    """
    global lastTime
    if (datetime.datetime.now() - lastTime).total_seconds() > (int(RefreshRate)/1000-1):
        lastTime = datetime.datetime.now()
        print("hi")
        for j in range(0, number):
            # create table for to display prices and time
            table = scrapers[j].getTable()
            df = pd.DataFrame(table)
            htmlChart = df.to_html(header=False, index=False)
            ProductName = "<h2>" + scrapers[j].getTitle() + "<h2>\n"
            html_head += ProductName + htmlChart
            global previous
            previous = html_head + html_end
    return previous

@app.route('/')
def home():
    return render_template_string(updateTables())

if __name__ == '__main__':
    app.run()
