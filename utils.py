import re

def clean_html(raw_html):
    """Remove html tag from a string"""
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext