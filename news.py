"""
A simple python bot that will return the articles from different website.
Sites : 
Nextinpact.com : - https://api-v1.nextinpact.com/api/v1/SimpleContent/list?Nb=:numberOfArticles&CategoriesIds=:id Get the last articles. CatgeoryName that interest me : Internet, Tech,        Logiciel, Culture Numérique => id = 3, 1, 2, 7
dev.to : webscrapping to get monthly news with custom #
catalins.tech : - https://hashnode.com/ajax/user/publication-entries?publication=5f25a0f4669da9610ee17e20&skip=0&limit=6 Get the articles before a certain publication
                - 5f25a0f4669da9610ee17e20 (the parameter in publication) is the author id that we want. skip is the number of articles before that we want to skip and limit is the number of articles that we want
hohanga.medium.com : - POST https://hohanga.medium.com/_/graphql Get the articles of the site. Don't work for the moment. Maybe need to make webscapping or maybe impossible
jackdomleo.dev : - https://jackdomleo.dev/_nuxt/content/db-2f7e0079.json
hashnode.com : - https://hashnode.com/ajax/posts/top Get the top articles
               - https://hashnode.com/ajax/user/fetch-trending-publications?category=week&page=0 Get the top publications of the week
scotch.io : Not found
css-tricks.com : - https://public-api.wordpress.com/rest/v1.3/sites/45537868/search?aggregations%5Bpost_type_1%5D%5Bterms%5D%5Bfield%5D=post_type&aggregations%5Bpost_type_1%5D%5Bterms%5D%5Bsize%5D=5&aggregations%5Bdate_histogram_2%5D%5Bdate_histogram%5D%5Bfield%5D=date&aggregations%5Bdate_histogram_2%5D%5Bdate_histogram%5D%5Binterval%5D=year&aggregations%5Btaxonomy_3%5D%5Bterms%5D%5Bfield%5D=tag.slug_slash_name&aggregations%5Btaxonomy_3%5D%5Bterms%5D%5Bsize%5D=5&aggregations%5Btaxonomy_0%5D%5Bterms%5D%5Bfield%5D=tag.slug_slash_name&aggregations%5Btaxonomy_0%5D%5Bterms%5D%5Bsize%5D=5&fields%5B0%5D=date&fields%5B1%5D=permalink.url.raw&fields%5B2%5D=tag.name.default&fields%5B3%5D=category.name.default&fields%5B4%5D=post_type&fields%5B5%5D=has.image&fields%5B6%5D=shortcode_types&fields%5B7%5D=image.url.raw&highlight_fields%5B0%5D=title&highlight_fields%5B1%5D=content&highlight_fields%5B2%5D=comments&filter%5Bbool%5D%5Bmust%5D%5B0%5D%5Bbool%5D%5Bshould%5D%5B0%5D%5Bterm%5D%5Bpost_type%5D=post&filter%5Bbool%5D%5Bmust%5D%5B0%5D%5Bbool%5D%5Bshould%5D%5B1%5D%5Bterm%5D%5Bpost_type%5D=page&filter%5Bbool%5D%5Bmust%5D%5B0%5D%5Bbool%5D%5Bshould%5D%5B2%5D%5Bterm%5D%5Bpost_type%5D=newsletters&filter%5Bbool%5D%5Bmust%5D%5B0%5D%5Bbool%5D%5Bshould%5D%5B3%5D%5Bterm%5D%5Bpost_type%5D=chapters&filter%5Bbool%5D%5Bmust%5D%5B1%5D%5Bbool%5D%5Bmust_not%5D%5B0%5D%5Bterm%5D%5Bpost_type%5D=attachment&filter%5Bbool%5D%5Bmust%5D%5B1%5D%5Bbool%5D%5Bmust_not%5D%5B1%5D%5Bterm%5D%5Bpost_type%5D=screenshot&query=&sort=score_default&size=11 Get articles
30secondsofcode.org : - https://www.30secondsofcode.org/page-data/index/page-data.json Get all the latest articles
                      - https://www.30secondsofcode.org/_next/data/0CtcJSwm7kL2jfV7Xviso/python/t/date/p/1.json Get python latest news
                      - Possible d'en trouver plus
jesuisundev.com : - French website. No API. Do webscrapping
"""
import time # Make break in our program
import sys # Use for exit
import settings # Get all the sources
from sources import * # Import our functions for each sources
import random # Make random choice
import requests # Make requests
# from clint.textui import colored # Colored text
import webbrowser # Open a new windows on browser

headers = settings.headers

def intro():
    print("  ______    ______   ______    __  __    _   __    ______ _       __   _____\n /_  __/   / ____/  / ____/   / / / /   / | / /   / ____/| |     / /  / ___/\n  / /     / __/    / /       / /_/ /   /  |/ /   / __/   | | /| / /   \__ \ \n / /     / /___   / /___    / __  /   / /|  /   / /___   | |/ |/ /   ___/ / \n/_/     /_____/   \____/   /_/ /_/   /_/ |_/   /_____/   |__/|__/   /____/  \n\n")
    print("\t\tKeep an eye on all digital news")
    print("\t\tMade by @Bastien750\n")
    time.sleep(1)

def menu():
    print("===================== Menu =====================\n")
    # print("What do you want to do ?\n")
    print("0 - Exit")
    print("1 - Get a random article")
    print("2 - Get a python article")

def handle_article(article):
    """Give informations about the article"""
    print("\n===================== Article =====================\n")
    print(f"{article.title.title()} - Author : {article.author} from {article.site}\n")
    print(article.description)
    print("")
    print(article.link)
    print("\n===================================================\n")
    print("Do you want to know more about this article ?")
    print("1 - Yes")
    print("2 - No")
    choice = int(input(""))
    if choice == 1:
        webbrowser.open_new(article.link)

def random_article(category):
    # list out keys and values separately and chose a random combine
    key_list = list(settings.categories[category].keys())
    site = random.choice(key_list)
    api_links = settings.categories[category][site]
    api_link = random.choice(api_links)
    data = requests.get(api_link, headers=headers).json()
    # Make our function executable
    func = globals()[site]
    article = func(data)
    handle_article(article)

def handle_choice(choice):
    if choice == 0:
        sys.exit("Good bye")
    elif choice == 1:
        random_article("all")
    elif choice == 2:
        random_article("python")

if __name__ == '__main__':
    intro()
    while True:
        menu()
        print("")
        choice = int(input("What's your choice ? "))
        print("")
        handle_choice(choice)