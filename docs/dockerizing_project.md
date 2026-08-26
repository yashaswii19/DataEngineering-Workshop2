# Dockerizing the Django Project

**Time box:** 11:15–01:00  
**Goal:** Run Django Admin inside Docker and connect Postgres (same habit as Workshop 1).

> Prefer the modern CLI: `docker compose` (with a space).  
> If that fails on your machine, try the older `docker-compose` (with a hyphen).  
> The file name stays `docker-compose.yml` either way.

- In order to dockerize the project we need to add a Dockerfile and a Docker Compose file as we have discussed in our previous workshop.
- Follow the below steps to achieve that.

1. Inside the root folder of the project create a folder called dockerfiles.

        mkdir dockerfiles
   
2. Get inside the folder and create a file called Dockerfile

        vi Dockerfile
3. Also create a `requirements.txt` file in the project root (`myworld/requirements.txt`) with:

        Django==4.2.16
        psycopg2-binary==2.9.9
        beautifulsoup4==4.12.3
        requests==2.32.3

4. Add the below content to the Dockerfile
      
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
5. Come out of the folder `dockerfiles` and create a docker-compose file in the project root folder.
    
        vi docker-compose.yml
6. Add the following content to that file
    
        services:
         web_service:
           build:
             context: ./
             dockerfile: ./dockerfiles/Dockerfile
           image: workshop2_web
           container_name: workshop_web_container
           stdin_open: true #  docker attach container_id
           tty: true
           ports:
            - "8000:8000"
           volumes:
            - .:/root/workspace/site

7. Go to the root folder of the project where the docker-compose file is present and bring the containers up
    
        docker compose up -d
- This will create a container workshop_web_container
8. Need to exec into that container.
    
        docker exec -it workshop_web_container sh
9. This will get into that container. You will now be inside the container and the working directory will be `/root/workspace/site`.
10. Run the command to run the server 
    
        python manage.py runserver 0:8000
    
    - Here we are binding the localhost to the port 8000.
    - Explore here [https://docs.djangoproject.com/en/3.2/ref/django-admin/#examples-of-using-different-ports-and-addresses](https://docs.djangoproject.com/en/3.2/ref/django-admin/#examples-of-using-different-ports-and-addresses)
11. Run http://127.0.0.1:8000/admin/ in the browser and now it should load the webpage.
12. Also open http://127.0.0.1:8000/members/ — you should see the Hello World template from the morning session.

# Adding Postgres service to our project

- Till now we were using the SQLite database which was supported in Django by default. Now let us connect postgres database to our Django project.
- We can run the postgres database as a separate service as we have done in our previous workshop.
- For that we need to update our current docker-compose file and add the new service to it. Add the following code to the docker-compose.yml file
    
         psql-db:
          image: 'postgres:14'
          container_name: psql-db
          environment:
            - PGPASSWORD=123456
            - POSTGRES_USER=postgres
            - POSTGRES_PASSWORD=123456
          ports:
            - '5432:5432'

- Also we should attach a volume to which our database need to be saved to. For that add the below lines at the bottom of the docker-compose.yml file.
  
        volumes:
          db:
            driver: local
- Now the whole content of the docker-compose.yml file should look like this

        services:
         web_service:
           build:
             context: ./
             dockerfile: ./dockerfiles/Dockerfile
           image: workshop2_web
           container_name: workshop_web_container
           stdin_open: true #  docker attach container_id
           tty: true
           ports:
            - "8000:8000"
           volumes:
            - .:/root/workspace/site
         
         psql-db:
          image: 'postgres:14'
          container_name: psql-db
          environment:
            - PGPASSWORD=123456
            - POSTGRES_USER=postgres
            - POSTGRES_PASSWORD=123456
          ports:
            - '5446:5432'
          volumes:
            - db:/var/lib/postgresql/data
  
        volumes:
          db:
            driver: local

- Now bring the containers up. 

        docker compose up -d
- Previously only one container was getting created. Now two containers will be created. 
    1. psql-db
    2. workshop_web_container
    
## Creating database

- Once the containers are up, exec into the database container ie., psql-db container.

        docker exec -it psql-db sh
- Now we need to login to postgres
    
        psql -U postgres
- Once we are logged into postgres we can run the sql command to create the database. Let us create a database called `member_db`

        CREATE DATABASE member_db;
- Adding the tables to this database can be done using the django models

## Adding tables using Django models

- As we have seen in the previous session, we can create tables using the Django models by running the migrate command.
- In order to do that we need to connect our existing Django app to the postgres database service.
- Following steps need to be followed for that.

1. We need to update the dockerfile to support postgres inside the workshop_web_container service. 
    
    - Update the Dockerfile in `dockerfiles/` so it installs from `requirements.txt` (already shown earlier in this guide). That file pins Django, psycopg2-binary, BeautifulSoup, and requests for the rest of today.
    - Rebuild after any Dockerfile / requirements change: `docker compose up --build -d`
    
2. Now we need to update the settings.py file present inside the `myworld` package folder (path: `myworld/myworld/settings.py`).
    
    - If you open the settings.py file inside that folder, you will find a section called DATABASES which will currently have the below content
    
            DATABASES = {
                'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
            }
    - The above content support the SQLite database. In order to support the postgres database we need to make the below changes
    
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.postgresql',
                    'NAME': 'member_db',
                    'USER': 'postgres',
                    'PASSWORD': '123456',
                    'HOST': 'psql-db',
                    'PORT': 5432,
                }
            }
    - 1. NAME should contain the name of the database you have created .
    - 2. USER, PASSWORD, and PORT should be the one which are mentioned in the postgres service of the docker-compose.yml file.
    - 3. HOST should be the name of the database container which is currently running.
    
3. Once the changes are made build the container again by running the below command

```buildoutcfg
docker compose up --build -d
```
4. This should build the images and bring both the containers up. Now exec into the workshop_web_container container and run the command to run migrations and create the tables from our model (Members if you followed the morning tutorial, or Students if you use the provided `myworld/` sample)
```buildoutcfg
python manage.py makemigrations
python manage.py migrate
```
5. This should have created the table in the member_db database. To check that, open a new tab in your terminal and go inside the project folder and exec into the database server

        docker exec -it psql-db sh
        psql -U postgres
        \c member_db
        \dt
    
    - The above commands should list down all the tables in the member_db and if the migration was success there should be a table called `members_members` (morning tutorial) or `members_students` (provided sample) added in the database along with other Django default tables.
    
6. In order to perform the CRUD operations, we will have to load the admin page. For that we will have to create a super user again since we have a new database now. Run the below command in the first tab where workshop_web_container container is running to create the user

        python manage.py createsuperuser
7. Once the user is created, we run our server. Run the below command
    
        python manage.py runserver 0:8000
8. Copy http://localhost:8000/admin in the web browser to load the web page and view the table and perform the CRUD operations.

## What's next today

After lunch we will **scrape a website** and **save scraped rows into Postgres**.
REST APIs, unit tests, and more advanced topics are in `docs/homework/` (after class).
