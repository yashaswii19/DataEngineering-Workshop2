import requests
# BUG for drill: wrong import (beautifulsoup4 package is imported as bs4)
from BeautifulSoup import BeautifulSoup

def start_extraction():
    print("Extraction started")
    url = "https://blog.python.org/"
    data = requests.get(url)
    page_soup = BeautifulSoup(data.text, 'html.parser')
    blogs = page_soup.select('div.date-outer')
    print("Found", len(blogs), "blogs")

if __name__ == "__main__":
    start_extraction()
