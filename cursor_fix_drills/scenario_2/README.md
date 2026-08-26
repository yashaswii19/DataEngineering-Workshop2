# Scenario 2 — Wrong CSS selector

## Goal

Run a scraper that finds **zero** posts, fix the selector with Cursor, then scrape real titles.

## Before you fix (expect empty result)

From this folder (`scenario_2/`):

```bash
python3 scrape_blogs.py
```

You should see something like:

```text
Found 0 blog cards.
FAIL: No blogs found. Check your CSS selectors.
```

## Fix with Cursor

1. Open Cursor Chat.
2. Paste this prompt:

```text
I am a beginner in Data Engineering Workshop 2, scenario 2.

I ran `python3 scrape_blogs.py` in cursor_fix_drills/scenario_2/ and it printed Found 0 blog cards / FAIL.

Please look only inside cursor_fix_drills/scenario_2/.
Fix the CSS selectors so the script finds blog cards on https://blog.python.org/ the same way as our workshop (article.post-card).
After the fix, `python3 scrape_blogs.py` should print SUCCESS and at least one title.

Do not change Workshop 1 or the main myworld project.
```

3. Apply the suggested changes in **this folder only**.

## After you fix (expect success)

```bash
python3 scrape_blogs.py
```

Expected:

```text
Found 8 blog cards.
SUCCESS: Scraping worked.
Title: ...
```

(The count may vary slightly if the website changes, but it should be greater than 0.)
