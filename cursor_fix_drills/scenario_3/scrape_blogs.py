"""Scrape blog cards from https://blog.python.org/."""

import sys

import requests

from BeautifulSoup import BeautifulSoup


def start_extraction() -> int:
    print("Extraction started")
    url = "https://blog.python.org/"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    page_soup = BeautifulSoup(response.text, "html.parser")
    blogs = page_soup.select("article.post-card")
    print(f"Found {len(blogs)} blog cards.")

    if len(blogs) == 0:
        print("FAIL: No blogs found.")
        return 1

    print("SUCCESS: Import and scrape worked.")
    return 0


if __name__ == "__main__":
    sys.exit(start_extraction())
