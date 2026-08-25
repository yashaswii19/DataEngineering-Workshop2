from bs4 import BeautifulSoup
import requests

def ping():
    html = "<html><body><div class='x'>ok</div></body></html>"
    soup = BeautifulSoup(html, "html.parser")
    print(soup.select_one("div.x").text)

if __name__ == "__main__":
    ping()
