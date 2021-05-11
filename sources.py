"""
Different functions that I use to handle each source
"""
from utils import *
import random # Make random choice
from article import Article

def nextinpact(data):
    """Handle data from nextinpact.com"""
    pass

def catalins(data):
    """Handle data from catalins.tech"""
    pass

def jackdomleo(data):
    """Handle data from jackdomleo.dev"""
    pass

def css_tricks(data):
    """Handle data from css-tricks.com"""
    pass

def thirtysecondsofcode(data):
    """Handle data from 30secondsofcode.org"""
    articles = data["pageProps"]["snippetList"]
    article = random.choice(articles)
    title = article["title"].replace("_", " ")
    description = clean_html(article["description"])
    author = "Isabelle Viktoria Maciohsek"
    site = "https://www.30secondsofcode.org"
    url = site + article["url"]
    return Article(title, description, author, site, url)