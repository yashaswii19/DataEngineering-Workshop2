import requests
from bs4 import BeautifulSoup

def start_extraction():
    print("Extraction started")
    url = "https://blog.python.org/"
    data = requests.get(url, timeout=30)
    page_soup = BeautifulSoup(data.text, 'html.parser')

    # BUG for drill: wrong selector (should be article.post-card)
    blogs = page_soup.select('article.post-card-WRONG')

    for blog in blogs:
        title_node = blog.select_one('h3')
        title = title_node.get_text(strip=True) if title_node else ""
        author_node = blog.select_one('span.font-medium')
        author = author_node.get_text(strip=True) if author_node else "Unknown"
        time_node = blog.select_one('time')
        date = time_node.get('datetime', '')[:10] if time_node else ""
        print(title, date, author)

if __name__ == "__main__":
    start_extraction()
