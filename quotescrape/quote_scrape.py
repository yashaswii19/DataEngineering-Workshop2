import requests
from bs4 import BeautifulSoup
import psycopg2

# PostgreSQL connection
conn = psycopg2.connect(
    dbname="quote_db",
    user="postgres",
    password="123456",
    host="localhost",
    port="5446"
)

cursor = conn.cursor()

base_url = "https://quotes.toscrape.com"
page = 1

while True:
    url = f"{base_url}/page/{page}/"

    print(f"Scraping page {page}...")

    response = requests.get(url, timeout=30)

    if response.status_code != 200:
        print("Failed:", response.status_code)
        break

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.select(".quote")

    if not quotes:
        break

    for quote in quotes:
        text = quote.select_one(".text").get_text(strip=True)
        author = quote.select_one(".author").get_text(strip=True)

        tags = [
            tag.get_text(strip=True)
            for tag in quote.select(".tag")
        ]

        tag_text = ", ".join(tags)

        cursor.execute(
            """
            INSERT INTO quotes (quote, author, tags)
            VALUES (%s, %s, %s)
            """,
            (text, author, tag_text)
        )

        print("Saved:", text)

    next_button = soup.select_one("li.next a")

    if not next_button:
        break

    page += 1

conn.commit()

cursor.close()
conn.close()

print("Scraping and database insertion completed!")
