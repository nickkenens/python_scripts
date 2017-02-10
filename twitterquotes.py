import sys

from bs4 import BeautifulSoup
from urllib import request

twitter_handles: [str] = ['philosophy_muse', 'tailopez']
quotes: [str] = []

def get_twitter_quotes() -> None:
    for handle in twitter_handles:
        twitter_link: str = create_twitter_url(handle)
        markup = request.urlopen(twitter_link)
        soup = BeautifulSoup(markup, 'html.parser')
        html_quotes = soup.find_all('p', attrs={'class': 'tweet-text'})
        for quote in html_quotes:
            quotes.append(quote.get_text())
        print_quotes()


def create_twitter_url(handle: str) -> str:
    return "https://twitter.com/" + handle

def print_quotes() -> None:
    for quote in quotes:
        print(quote)

get_twitter_quotes()
