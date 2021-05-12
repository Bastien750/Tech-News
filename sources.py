"""
Different functions that handle each source
"""
from utils import *
import random # Make random choice
from article import Article
import requests
import settings

def nextinpact(data):
    """Handle data from nextinpact.com"""
    articles = data["results"]
    article = random.choice(articles)
    title = article["title"]
    description = article["introTextMeta"]
    authors = article["authors"]
    if len(authors) == 0:
        author = "Unknow"
    else:
        author = ""
        for auth in authors:
            name = auth["name"]
            author += f"{name} -"
    site = "https://www.nextinpact.com/"
    url = site + "lebrief/" + str(article["contentId"]) + "/" + article["seoUrl"]
    return Article(title, description, author, site, url)

def catalins(data):
    """Handle dara from catalins.tech"""
    articles = data["posts"]
    article = random.choice(articles)
    title = article["title"]
    description = article["brief"]
    author = article["author"]["name"]
    site = "https://catalins.tech/"
    url = site + article["slug"]
    return Article(title, description, author, site, url)

def jackdomleo(data):
    """Handle data from jackdomleo"""
    articles = data["_collections"][0]["_data"]
    article = random.choice(articles)
    title = article["title"]
    description = article["description"]
    author = "@jackdomleo7"
    site = "https://jackdomleo.dev/"
    url = article["devtoLink"]
    return Article(title, description, author, site, url)

def hashnode(data):
    """Handle data from hashnode.com"""
    try:
        """Only for top articles"""
        articles = data["posts"]
        article = random.choice(articles)
        title = article["title"]
        description = article["brief"]
        author = article["author"]["name"]
        site = "https://hashnode.com/"
        url = article["publication"]["domain"] + "/" + article["slug"]
        return Article(title, description, author, site, url)
    except:
        """For top authors of the week"""
        authors = data["result"]
        author = random.choice(authors)
        author_id = author["author"]["_id"]
        data = requests.get(f"https://hashnode.com/ajax/user/more-posts-from-author?exclude={author_id}", headers=settings.headers).json()
        return hashnode(data)

def css_tricks(data):
    """Handle data from css-tricks.com"""
    articles = data["results"]
    article = random.choice(articles)
    title = article["highlight"]["title"][0]
    description = article["highlight"]["content"][0]
    if not description:
        description = "No description found for this article"
    author = "Unknow" # Not in the API results
    site = "https://css-tricks.com/"
    url = article["fields"]["permalink.url.raw"]
    return Article(title, description, author, site, url)

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

def kitze(data):
    """Handle data from kitze.io"""
    articles = data["pageProps"]["posts"]
    article = random.choice(articles)
    title = article["title"]
    description = article["metaDescription"]
    if not description:
        description = "No description found for this article"
    author = "@thekitze"
    site = "https://kitze.io"
    url = site + "/posts/" + article["slug"]
    return Article(title, description, author, site, url)

def hemdan(data):
    """Handle data from hemdan.hashnode.dev"""
    articles = data["posts"]
    article = random.choice(articles)
    title = article["title"]
    description = article["brief"]
    author = article["author"]["name"]
    site = "https://hemdan.hashnode.dev/"
    url = site + article["slug"]
    return Article(title, description, author, site, url)

def robkendal(data):
    """Handle data from robkendal.co.uk"""
    articles = data["pageProps"]["allPostsData"]
    article = random.choice(articles)
    title = article["title"]
    description = article["description"]
    author = "Rob Kendal"
    site = "https://robkendal.co.uk/"
    url = site + "blog/" + article["id"]
    return Article(title, description, author, site, url)

def dailydev(data):
    """Handle data from daily.dev"""
    articles = data["data"]["feed"]["edges"]
    article = random.choice(articles)["node"]
    title = article["title"]
    description = title + "..."
    if not article["author"]:
        author = "Unknow"
    else:
        author = article["author"]["name"] # Get the name if author is not null
    site = "https://daily.dev/"
    url = article["url"]
    return Article(title, description, author, site, url)