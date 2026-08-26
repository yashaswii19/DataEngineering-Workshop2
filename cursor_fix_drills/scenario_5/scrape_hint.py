from bs4 import BeautifulSoup


def main() -> None:
    html = "<html><body><div class='ok'>SUCCESS: BeautifulSoup is available and working.</div></body></html>"
    soup = BeautifulSoup(html, "html.parser")
    print(soup.select_one("div.ok").get_text(strip=True))


if __name__ == "__main__":
    main()
