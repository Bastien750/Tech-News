import random

sources_list = ["nextinpact", "catalins", "jackdomleo", "css_tricks", "thirtysecondsofcode"],

sources = {
    "nextinpact" : [
        "https://api-v1.nextinpact.com/api/v1/SimpleContent/list?Nb=100&CategoriesIds=1", # Tech
        "https://api-v1.nextinpact.com/api/v1/SimpleContent/list?Nb=100&CategoriesIds=2", # Logiciel
        "https://api-v1.nextinpact.com/api/v1/SimpleContent/list?Nb=100&CategoriesIds=3", # Internet
        "https://api-v1.nextinpact.com/api/v1/SimpleContent/list?Nb=100&CategoriesIds=7" # Culture numérique
    ],
    "catalins" : [
        "https://hashnode.com/ajax/user/publication-entries?publication=5f25a0f4669da9610ee17e20&skip=0&limit=100", # Get the 100 last publications from catalins
    ],
    "jackdomleo": [
        "https://jackdomleo.dev/_nuxt/content/db-2f7e0079.json", # Get all the articles
    ],
    "hashnode": [
        "https://hashnode.com/ajax/posts/top", # Get the top articles of the site
        "https://hashnode.com/ajax/user/fetch-trending-publications?category=week&page=0", # Get the top publications of the week (can edit the number of the page)
    ],
    "css_tricks": [
        "https://public-api.wordpress.com/rest/v1.3/sites/45537868/search?aggregations%5Bpost_type_1%5D%5Bterms%5D%5Bfield%5D=post_type&aggregations%5Bpost_type_1%5D%5Bterms%5D%5Bsize%5D=5&aggregations%5Bdate_histogram_2%5D%5Bdate_histogram%5D%5Bfield%5D=date&aggregations%5Bdate_histogram_2%5D%5Bdate_histogram%5D%5Binterval%5D=year&aggregations%5Btaxonomy_3%5D%5Bterms%5D%5Bfield%5D=tag.slug_slash_name&aggregations%5Btaxonomy_3%5D%5Bterms%5D%5Bsize%5D=5&aggregations%5Btaxonomy_0%5D%5Bterms%5D%5Bfield%5D=tag.slug_slash_name&aggregations%5Btaxonomy_0%5D%5Bterms%5D%5Bsize%5D=5&fields%5B0%5D=date&fields%5B1%5D=permalink.url.raw&fields%5B2%5D=tag.name.default&fields%5B3%5D=category.name.default&fields%5B4%5D=post_type&fields%5B5%5D=has.image&fields%5B6%5D=shortcode_types&fields%5B7%5D=image.url.raw&highlight_fields%5B0%5D=title&highlight_fields%5B1%5D=content&highlight_fields%5B2%5D=comments&filter%5Bbool%5D%5Bmust%5D%5B0%5D%5Bbool%5D%5Bshould%5D%5B0%5D%5Bterm%5D%5Bpost_type%5D=post&filter%5Bbool%5D%5Bmust%5D%5B0%5D%5Bbool%5D%5Bshould%5D%5B1%5D%5Bterm%5D%5Bpost_type%5D=page&filter%5Bbool%5D%5Bmust%5D%5B0%5D%5Bbool%5D%5Bshould%5D%5B2%5D%5Bterm%5D%5Bpost_type%5D=newsletters&filter%5Bbool%5D%5Bmust%5D%5B0%5D%5Bbool%5D%5Bshould%5D%5B3%5D%5Bterm%5D%5Bpost_type%5D=chapters&filter%5Bbool%5D%5Bmust%5D%5B1%5D%5Bbool%5D%5Bmust_not%5D%5B0%5D%5Bterm%5D%5Bpost_type%5D=attachment&filter%5Bbool%5D%5Bmust%5D%5B1%5D%5Bbool%5D%5Bmust_not%5D%5B1%5D%5Bterm%5D%5Bpost_type%5D=screenshot&query=&sort=score_default&size=11",# Get articles from the site css-tricks
    ],
    "thirtysecondsofcode": [
        "https://www.30secondsofcode.org/page-data/index/page-data.json", # Get the latest articles
        f"https://www.30secondsofcode.org/_next/data/0CtcJSwm7kL2jfV7Xviso/python/p/{random.randint(1, 11)}.json" # Get python latest news
    ],  
}

categories = {
    "all": sources,
    "python": {"thirtysecondsofcode": [sources["thirtysecondsofcode"][1], ]},
}