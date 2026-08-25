"""Scrape blog cards from https://blog.python.org/ and print titles."""

import sys

import requests
from bs4 import BeautifulSoup


def start_extraction() -> int:
    print("Extraction started")
    url = "https://blog.python.org/"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    page_soup = BeautifulSoup(response.text, "html.parser")

    # Selector must match the live site cards.
    blogs = page_soup.select("article.post-card-WRONG")
    print(f"Found {len(blogs)} blog cards.")

    if len(blogs) == 0:
        print("FAIL: No blogs found. Check your CSS selectors.")
        return 1

    for blog in blogs:
        title_node = blog.select_one("h3")
        title = title_node.get_text(strip=True) if title_node else "(no title)"
        print("Title:", title)

    print("SUCCESS: Scraping worked.")
    return 0


if __name__ == "__main__":
    sys.exit(start_extraction())
