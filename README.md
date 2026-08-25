# Data Engineering Workshop 2

A one-day beginner workshop covering a simple Django project, web scraping into PostgreSQL, Cursor Skills, and guided fix drills.

## Prerequisites

### Before you start

- Complete **Workshop 1** (Docker basics, simple web scraping, PostgreSQL basics, Git basics)
- Keep the same machine setup from Workshop 1 ready to use

### Software

- Python 3.9 or above (`pip3` available)
- Docker and Docker Compose
- Git (any recent version)
- [Cursor](https://cursor.com/) installed (required for the Skills and fix-drill sessions)

### Project setup

- A Git account (GitHub or GitLab — the same one from Workshop 1 is fine)
- Open this Workshop 2 folder in Cursor on workshop day
- Use the provided `myworld/` sample project. Do **not** run `django-admin startproject myworld` inside this folder (it already exists and would conflict)
- Prefer `docker compose` (space). Older machines may still have `docker-compose` (hyphen). The file name is always `docker-compose.yml`

### Quick checks

Run these in a terminal:

```bash
python3 --version
git --version
docker --version
docker compose version || docker-compose --version
```

All commands should print a version without errors. Cursor should open this project successfully.

## Learning outcomes

By the end of this workshop, you will be able to:

- Explain Django at a beginner level and run a simple Dockerized Django Admin project
- Scrape a workshop-style page ([Python Insider](https://blog.python.org/)) and store rows in PostgreSQL
- Explain what a Cursor Skill file is and when to use one
- Use the workshop scraper Skill with a URL and store data in the expected database tables
- Use Cursor with five provided prompts to fix common beginner errors

## About Cursor in this workshop

We use **Cursor** as the editor. In the afternoon you will:

1. Use a **Skill** (a `SKILL.md` file with project-specific instructions)
2. Paste prompts into **Cursor Chat** so Cursor can follow that Skill and help fix code

You do not need to build a separate custom agent. “Cursor Chat” is the built-in AI chat in Cursor (sometimes labeled Agent). Skills tell that chat how to work for *this* project.

## Schedule

| Time | Topics |
|------|--------|
| 09:00–09:45 | [Introduction to Django](docs/introduction_to_django.md) |
| 09:45–11:15 | [Creating a Django Project](docs/creating_a_django_project.md) |
| 11:15–01:00 | [Dockerizing the project](docs/dockerizing_project.md) |
| 01:00–02:00 | Lunch |
| 02:00–03:15 | [Web scraping using Python](docs/webscraping_using_python.md) |
| 03:15–04:15 | [Saving scraped data in Postgres](docs/saving_in_postgres_db.md) |
| 04:15–04:40 | [What is a Skill + scrape Skill](docs/introduction_to_skills.md) |
| 04:40–05:00 | [Cursor fix drills](docs/cursor_fix_drills.md) |
| After class | [Homework](docs/homework/README.md) |

## Project layout

| Path | Purpose |
|------|---------|
| `myworld/` | Live Django project and scraper |
| `.cursor/skills/workshop-blog-scraper/` | Workshop scraper Skill |
| `cursor_fix_drills/` | Runnable fix drills (fail → fix with Cursor → succeed) |
| `docs/` | Step-by-step guides for each session |
| `docs/homework/` | Optional topics for after class |
| `vulnerability.txt` | Notes about demo passwords (lab use only) |

## If time is short

Complete in this order: scrape → save to PostgreSQL → Skill demo. Fix drills can be completed quickly by pasting the prompt from each scenario `README.md` and checking the result.
