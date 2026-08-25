# Save the scraped data to Postgres Database

**Time box:** 03:15–04:15  
**Goal:** Create the `Blog` model / `members_blog` table and insert scraped rows into Postgres.

- Now let us save the data that we have extracted now into a postgres database.
- Let us use the same database `member_db` that we created earlier today to save the data.
- If you have not created the mentioned database, follow the below step to create the database.

1. Open a new tab in your terminal and exec into the psql-db container. Since you have run the `docker compose up` command 
before, both workshop_web_container and psql-db containers should be up. So we need not bring the container up. We can directly 
   run the below command to exec into the container
   
        docker exec -it psql-db sh

    - Please note that psql-db and workshop_web_container are the container_name that you have mentioned in the 
docker-compose.yml file. If the names you have specified is different, use that.
    
2. Now run the below commands to login to psql.

       psql -U postgres
3. Now create the database by running below command.

       CREATE DATABASE member_db;

<hr/>

- Since the database is ready, let's create the required tables and columns to that database using the Django models. Keep the database container
  running in this tab and you may continue the development in a new tab.
- Follow the below steps:

1. Open the models.py file which is present in the members folder. 

      
     File path : myworld/members/models.py

     vi models.py
        or
     gedit models.py

2. If you use the provided `myworld/` sample, you already have one model **Students** in that file (the morning from-scratch tutorial used **Members** — either is fine for learning). Let's add one more model called Blog into the same file.
For that append the below code to that file
   
```buildoutcfg
class Blog(models.Model):
    title = models.CharField(max_length=500)
    release_date = models.DateTimeField('Release Date')
    blog_time = models.CharField(max_length=50)
    author = models.CharField(max_length=200)
    created_date = models.DateTimeField('Created Date', auto_now_add=True, null=True)
   
    def __str__(self):                               
        return self.title
```

  - Now models.py will look like this

 ```buildoutcfg
from django.db import models
   
BRANCH_CHOICES = (
    ("BA", "BA"),
    ("B.COM", "B.COM"),
    ("MBA", "MBA"),
    ("CA", "CA"),
)
         
# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    roll_number = models.IntegerField()
    mobile = models.CharField(max_length=10)
    branch = models.CharField(max_length=10, choices=BRANCH_CHOICES, null=True)
         
    def __str__(self):
        return self.first_name + " " + self.last_name
         
class Blog(models.Model):
    title = models.CharField(max_length=500)
    release_date = models.DateTimeField('Release Date')
    blog_time = models.CharField(max_length=50)
    author = models.CharField(max_length=200)
    created_date = models.DateTimeField('Created Date', auto_now_add=True, null=True)
             
    def __str__(self):                               
        return self.title
```

   
   - Each class represents a model which will in turn represent a table in the database and each property of that class refers to
each columns in that table.
     
3. Let us run makemigrations to create the database table using the models. For that first open the tab where workshop_web_container is running.
If it is not running anywhere, open a new tab and run the below command to run the container
   
       docker exec -it workshop_web_container sh
  - Keep the container running in the tab. Anymore if you have to modify any other files you can open a new tab. Right now 
you should have to 2 tabs where in one workshop_web_container should be running and in other psql-db container should be running.
    
4. Once you get inside workshop_web_container, run the below commands

        python manage.py makemigrations
        python manage.py migrate
5. Now go to the psql-db (database container) and run below commands to ensure that the new table members_blog is created.

        postgres=# \c member_db
        You are now connected to database "member_db" as user "postgres".
   
        member_db=# \dt
  - The above command should list down all the tables in the member_db and there should be members_blog present.
    
        \d members_blog
  - This command should describe the members_blog table and show all the columns present.

<hr/>

- Now let us modify our script so that it will start saving the extracted data into the created table.
- Open the web_scrapper.py file present in the myworld folder and replace the script with the one given below.

```buildoutcfg
"""
Workshop scraper for https://blog.python.org/

What this script does (beginner summary):
1) Connects to the workshop Postgres database
2) Clears old rows in members_blog (TRUNCATE ... CASCADE)
3) Downloads the Python Insider homepage
4) Finds each blog card (article.post-card)
5) Reads title, author, and date/time
6) Inserts each row into members_blog
"""

import psycopg2
import requests
from bs4 import BeautifulSoup

# For the credentials mentioned below, you may refer the docker-compose.yml present in myworld .
db_name = 'member_db'
db_user = 'postgres'
db_pass = '123456'
db_host = 'psql-db'
db_port = '5432'

conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host, port=db_port)


def add_row_to_blog(title, author, date, time):
    sql = """INSERT INTO members_blog (title, release_date, blog_time, author, created_date) VALUES (%s, %s::DATE, %s::TIME, %s, NOW())"""
    with conn:
        with conn.cursor() as curs:
            curs.execute(sql, (title, date, time, author))


def truncate_table():
    with conn:
        with conn.cursor() as curs:
            curs.execute("TRUNCATE members_blog CASCADE;")


def start_extraction():
    print("Extraction started")
    url = "https://blog.python.org/"
    truncate_table()
    data = requests.get(url, timeout=30)
    page_soup = BeautifulSoup(data.text, 'html.parser')
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
            date = time_node.get_text(strip=True) if time_node else "1970-01-01"
            time = "00:00:00"

        add_row_to_blog(title, author, date, time)

        print("\nTitle:", title)
        print("Date:", date)
        print("Time:", time)
        print("Author:", author)
        print(
            "\n---------------------------------------------------------------------------------------------------------------\n"
        )


if __name__ == "__main__":
    start_extraction()
```

  - The main upgrade from the print-only script: database connection, `TRUNCATE members_blog CASCADE;`, and `INSERT` into `members_blog`.
    
<hr/>

    
- Now go to workshop_web_container container and run the script

      python3 web_scrapper.py
- Once the script run completes, go to the database container and run the below sql query to check if the data is populated or not.

      select * from members_blog;

- You can also open Django Admin at http://127.0.0.1:8000/admin/ (after `createsuperuser` and `runserver`) and open **Blogs** to see the same rows.

## Note about TRUNCATE

When the scraper clears old rows it uses:

      TRUNCATE members_blog CASCADE;

Do **not** add `RESTART IDENTITY` — that can break related keys in more complex databases later.

## What's next today

Next we learn **what a Cursor Skill is** and use our workshop scraper Skill.
Django views that wrap the scraper, date-range extractors, and debugging topics are in `docs/homework/` (after class).
