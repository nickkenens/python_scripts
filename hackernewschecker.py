import sys

# Import BeautifulSoup for HTML Parsing
from bs4 import BeautifulSoup
from urllib import request

hackernews_url = "https://news.ycombinator.com/"

def getHackerNewsHeadlines():
    markup = getHackerNewsMarkup()
    headlines = markup.find_all('a', attrs={'class': 'storylink'})

    headline_titles = []
    headline_hrefs = []

    for headline in headlines:
        headline_hrefs.append(headline['href'])
        headline_titles.append(headline.get_text())

    for headline in headline_titles:
        print(headline)

def getHackerNewsMarkup():
    hackernews_markup = request.urlopen(hackernews_url)
    return BeautifulSoup(hackernews_markup, 'html.parser')

getHackerNewsHeadlines()