# Scenario 3 — Broken import

## Goal

See a real Python import error, fix it with Cursor, then run the script successfully.

## Before you fix (expect ImportError)

From this folder (`scenario_3/`):

```bash
python3 scrape_blogs.py
```

You should see an error like:

```text
ModuleNotFoundError: No module named 'BeautifulSoup'
```

or `ImportError`.

## Fix with Cursor

1. Open Cursor Chat.
2. Paste this prompt:

```text
I am a beginner in Data Engineering Workshop 2, scenario 3.

I ran `python3 scrape_blogs.py` in cursor_fix_drills/scenario_3/ and Python failed with an import error for BeautifulSoup.

Please look only inside cursor_fix_drills/scenario_3/.
Fix the import so BeautifulSoup works the same way as in our workshop (`from bs4 import BeautifulSoup`).
After the fix, `python3 scrape_blogs.py` should print SUCCESS.

Do not change Workshop 1 or the main myworld project.
```

3. Apply the suggested changes in **this folder only**.

## After you fix (expect success)

```bash
python3 scrape_blogs.py
```

Expected:

```text
Found ... blog cards.
SUCCESS: Import and scrape worked.
```
