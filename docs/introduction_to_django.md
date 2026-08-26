# Introduction to Django (Simple Overview)

**Time box:** 09:00–09:45  
**Goal:** Understand what Django is and the MVT idea before we create a small project.

Django is a Python framework that makes it easier to create web sites using Python.
It comes with ready-to-use features like an admin login, database connection, and CRUD operations (Create, Read, Update, Delete).

Today we keep Django **simple**. You only need the big picture — then we will build a small project step by step.

<br />

## How does Django Work?

Django follows the MVT design pattern (Model View Template).

- **Model** — the data you want to present (usually from a database)
- **View** — a request handler that chooses what content to return
- **Template** — an HTML-like file that describes how the page looks

## Model (short)

- Models live in `models.py`.
- Django’s ORM lets you work with tables using Python instead of writing lots of SQL by hand.

## View (short)

- Views live in `views.py`.
- A view receives an HTTP request and returns a response (often by rendering a template).

## Template (short)

- Templates live in a `templates` folder.
- They use HTML plus Django tags, for example:

```
<h1>My Homepage</h1>
<p>My name is {{ firstname }}.</p>
```

## URLs (short)

- `urls.py` maps a URL path to a view.
- When a user opens a URL, Django finds the matching view and runs it.

## Generic workflow

1. Django receives the URL, checks `urls.py`, and calls the matching view.
2. The view may load data from models.
3. The view sends data to a template.
4. The template returns finished HTML to the browser.

![Django Workflow](django-mvt-based-control-flow.png)

> Optional extra reading: [https://www.w3schools.com/django/django_intro.php](https://www.w3schools.com/django/django_intro.php)

## What's next today

Next we **create a simple Django project** and open Django Admin.
After lunch we focus on **web scraping** and **Postgres**.
REST APIs, unit tests, and more advanced topics are in `docs/homework/` (after class).
