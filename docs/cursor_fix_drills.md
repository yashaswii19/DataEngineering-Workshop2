# Cursor fix drills

**Session goals:** Practice a real failure → fix with Cursor → success loop on common beginner bugs.

## How each drill works

For every scenario:

1. **Run the “Before you fix” commands** in that scenario’s `README.md` and watch it fail.
2. Paste the prompt from that scenario’s `README.md` into **Cursor Chat** and apply the fix in that scenario folder.
3. **Run the “After you fix” commands** and confirm you see `SUCCESS`.

Work only inside `cursor_fix_drills/scenario_N/`. Do not change Workshop 1 or the main `myworld/` project unless your instructor says otherwise.

## Requirements

- Python packages used earlier today (`requests`, `beautifulsoup4`, `psycopg2-binary`) available on your machine for scenarios 1–4
- Docker available for scenarios 1 and 5
- Internet access for scenarios 2 and 3 (they call https://blog.python.org/)

## Scenarios

| # | Topic | Folder |
|---|--------|--------|
| 1 | Wrong Postgres password / mismatch | [scenario_1](../cursor_fix_drills/scenario_1/) |
| 2 | Wrong CSS/HTML selector in scraper | [scenario_2](../cursor_fix_drills/scenario_2/) |
| 3 | Broken Python import | [scenario_3](../cursor_fix_drills/scenario_3/) |
| 4 | Model field vs insert name mismatch | [scenario_4](../cursor_fix_drills/scenario_4/) |
| 5 | Missing package in requirements/Dockerfile | [scenario_5](../cursor_fix_drills/scenario_5/) |

## After class

More topics (REST, unit tests, Django views, extractors, debugging) are in [homework](homework/README.md).
