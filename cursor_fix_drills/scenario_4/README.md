# Scenario 4 — Model field vs insert column mismatch

## Goal

See a real SQL error when inserting a blog row, fix the field/column name with Cursor, then insert successfully.

## Before you fix (expect SQL error)

From this folder (`scenario_4/`):

```bash
python3 run_insert.py
```

You should see an error such as:

```text
ERROR: insert failed
... no such column: titel ...
```

or similar wording about an unknown column.

## Fix with Cursor

1. Open Cursor Chat.
2. Paste this prompt:

```text
I am a beginner in Data Engineering Workshop 2, scenario 4.

I ran `python3 run_insert.py` in cursor_fix_drills/scenario_4/ and the insert failed because a column/field name does not match.

Please look only inside cursor_fix_drills/scenario_4/.
Fix the mismatch between `models_helpers.py` and `insert_helpers.py` so the column names agree (`title`, not a typo).
After the fix, `python3 run_insert.py` should print SUCCESS.

Do not change Workshop 1 or the main myworld project.
```

3. Apply the suggested changes in **this folder only** (especially `insert_helpers.py`).

## After you fix (expect success)

```bash
python3 run_insert.py
```

Expected:

```text
SUCCESS: Row inserted into blogs table.
title=Hello Workshop | author=Student
```
