# Web Scraping Using Python

**Time box:** 02:00–03:15  
**Goal:** Scrape [Python Insider](https://blog.python.org/) and print title, date, time, and author.

- Let us scrape the website [Python Insider](https://blog.python.org/).
- Following data need to be extracted out of the website.
    1. Title 
    2. Release Date
    3. Blog Time
    4. Author

> Note for instructors/students: the Python Insider site layout was redesigned. This workshop uses `article.post-card` selectors (not the old `div.date-outer` Blogger layout).

> If `myworld/web_scrapper.py` already exists with Postgres insert code, replace its contents with the **print-only** script below for this session. The next session puts the database version back.
    
- We will first write a simple python script to extract and print the above mentioned data from the website.
- Follow the given steps in order to achieve that.

1. Open the project `myworld` in this repository (`DataEngineering-Workshop2/myworld/`).
2. Create or open `web_scrapper.py` for the print-only scraper.

        vi web_scrapper.py 
            or
        gedit web_scrapper.py

3. Write the below script inside that file.
```buildoutcfg
import requests
from bs4 import BeautifulSoup

def start_extraction():
    print("Extraction started")
    url = "https://blog.python.org/"
    data = requests.get(url, timeout=30)
    page_soup = BeautifulSoup(data.text, 'html.parser')

    # Each blog card on the redesigned Python Insider homepage
    blogs = page_soup.select('article.post-card')

    for blog in blogs:
        title_node = blog.select_one('h3')
        title = title_node.get_text(strip=True) if title_node else ""

        author_node = blog.select_one('span.font-medium')
        author = author_node.get_text(strip=True) if author_node else "Unknown"

        time_node = blog.select_one('time')
        if time_node and time_node.get('datetime'):
            iso_value = time_node['datetime']
            date = iso_value[:10]
            time = iso_value[11:19] if len(iso_value) >= 19 else "00:00:00"
        else:
            date = time_node.get_text(strip=True) if time_node else "unknown"
            time = "00:00:00"

        print("\nTitle:", title)
        print("Date:", date)
        print("Time:", time)
        print("Author:", author)
        print("\n---------------------------------------------------------------------------------------------------------------\n")


if __name__ == "__main__":
    start_extraction()
```
         

4. Our Docker image already installs packages from `myworld/requirements.txt` (Django, psycopg2-binary, beautifulsoup4, requests).
   If you changed `requirements.txt` or the Dockerfile, rebuild:

       docker compose up --build -d

   Example Dockerfile used by this workshop:

```buildoutcfg
FROM python:3.10.2-alpine3.15
RUN apk update && \
    apk --no-cache add --virtual build-deps-alpine build-base && \
    apk --no-cache add --virtual postgresql-deps libpq-dev
RUN pip install --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN mkdir -p /root/workspace/src
COPY ./  /root/workspace/site
WORKDIR /root/workspace/site
```

5. Once the containers are up, exec into `workshop_web_container`.
   
       docker exec -it workshop_web_container sh
6. Run the below command to run the python script.
         
       python3 web_scrapper.py
7. Now you should be able to see the extracted data printed in your screen.

## Expected idea of output

You should see several blocks like:

```text
Title: Some blog title
Date: 2026-06-23
Time: 00:00:00
Author: Some Name
```

## What's next today

Next we **save this scraped data into Postgres**.
