# Amazon Price Tracking and Email Notifications

This Python project tracks items, checks their status periodically, and sends email notifications to alert users of price changes.


## Dependencies

Before running the project, make sure you have the following dependencies installed:

- [pandas](https://pandas.pydata.org/): `$ pip install pandas`
- [urllib](https://pypi.org/project/urllib3/): `$ pip install urllib3`
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): `$ pip install beautifulsoup4`

## Installation
1. Clone the repository
```commandline
https://github.com/y3llowfellow/WebScraper
```
2. Run the code via Command Line
```commandline
python [filepath]\WebScraper\PriceTracker.py
```

## Usage and Command Line Arguments

The script `PriceTracker.py` takes the following command-line arguments:

1. `num_items` (int): Number of items to track.
2. `interval_ms` (int): Milliseconds between price checks.
3. `email` (str): Email address to send notifications.

Then, the program will prompt users to enter the Amazon links of the prices they wish to track. See the following example
```
Enter item 1 url: https://www.amazon.com/...
```

## Example

```python PriceTracker.py 10 5000 example@example.com```

This command will track 10 items, checking every 5000 milliseconds (5 seconds), and sending emails to `example@example.com`. Adjust the values as needed.

## Licensing and Credits
All credits go to Colin Shen and Cody Wang!

