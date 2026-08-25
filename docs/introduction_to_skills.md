# What is a Cursor Skill?

**Session goals:** Learn what a Skill file is, then use our workshop Skill to scrape a URL into PostgreSQL.

## What is a Skill file?

A **Skill** is a small set of instructions (usually a `SKILL.md` file) that tells Cursor how to do a **specific, repeatable task** the way *this project* expects.

Think of it as a checklist Cursor should follow — not a one-off free-form answer.

## Common uses of Skills

- Follow project conventions (folders, naming, database settings)
- Generate a scraper that matches our workshop pattern
- Review or fix code using a known checklist
- Avoid inventing a different database or table layout

## Do we use “agents”?

We use **Cursor Chat** (the built-in AI chat in Cursor; the UI may label it **Agent**).

We are **not** asking you to create a separate custom agent product. The Skill file guides Cursor Chat for this workshop project.

## Where our Skill lives

```text
DataEngineering-Workshop2/
  .cursor/skills/workshop-blog-scraper/SKILL.md
```

Cursor can discover project Skills under `.cursor/skills/`.

## How to use it

1. Open this Workshop 2 folder in Cursor.
2. Open **Cursor Chat**.
3. Paste the prompt below (you may change the URL if asked to try a similar page).
4. Cursor should follow the Skill: write or update a runnable script under `myworld/` and explain each step briefly.
5. Run the script inside `workshop_web_container` the same way you ran `web_scrapper.py`.
6. Verify rows in PostgreSQL:

```sql
SELECT title, author FROM members_blog LIMIT 5;
```

## Copy-paste prompt

```text
Use the workshop-blog-scraper skill.
Scrape this URL: https://blog.python.org/
Write a Python script under myworld/ that stores title, release date, blog time, and author
into our workshop Postgres database (member_db / members_blog) the same way web_scrapper.py does.
Explain each step briefly for a beginner.
```

## What success looks like

- A script exists under `myworld/`
- Running it inserts rows into `members_blog`
- Cursor briefly explains selectors and the database insert for beginners

## Next

Practice fixing common beginner bugs with Cursor using the five short drills.
