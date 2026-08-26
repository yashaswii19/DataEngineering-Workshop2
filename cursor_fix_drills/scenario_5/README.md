# Scenario 5 — Missing package in requirements

## Goal

See a container fail because BeautifulSoup is missing, add the package with Cursor’s help, then run successfully.

## Before you fix (expect ModuleNotFoundError)

From this folder (`scenario_5/`):

```bash
docker build -t drill5_scrape .
docker run --rm drill5_scrape
```

You should see an error like:

```text
ModuleNotFoundError: No module named 'bs4'
```

## Fix with Cursor

1. Open Cursor Chat.
2. Paste this prompt:

```text
I am a beginner in Data Engineering Workshop 2, scenario 5.

I ran `docker build -t drill5_scrape .` and `docker run --rm drill5_scrape` in cursor_fix_drills/scenario_5/.
The container fails with `ModuleNotFoundError: No module named 'bs4'`.

Please look only inside cursor_fix_drills/scenario_5/.
Fix `requirements.txt` (and Dockerfile only if needed) so BeautifulSoup installs.
Explain that the pip package name is `beautifulsoup4` while the import name is `bs4`.
After the fix, rebuilding and running should print SUCCESS.

Do not change Workshop 1 or the main myworld project.
```

3. Apply the suggested changes in **this folder only** (usually `requirements.txt`).

## After you fix (expect success)

```bash
docker build -t drill5_scrape .
docker run --rm drill5_scrape
```

Expected:

```text
SUCCESS: BeautifulSoup is available and working.
```
