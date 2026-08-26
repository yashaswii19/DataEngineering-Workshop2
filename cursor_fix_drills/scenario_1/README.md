# Scenario 1 — Database password mismatch

## Goal

See a real database connection failure, fix the mismatch with Cursor, then connect successfully.

## Before you fix (expect failure)

From this folder (`scenario_1/`):

```bash
docker compose down -v
docker compose up -d
sleep 5
python3 test_connection.py
```

You should see an error such as **password authentication failed** or **could not connect**.

## Fix with Cursor

1. Open Cursor Chat.
2. Paste this prompt:

```text
I am a beginner in Data Engineering Workshop 2, scenario 1.

I ran `docker compose up -d` and then `python3 test_connection.py` in cursor_fix_drills/scenario_1/ and the database connection failed.

Please look only inside cursor_fix_drills/scenario_1/.
Find why the password/settings do not match, fix the files so `python3 test_connection.py` prints SUCCESS, and tell me the exact commands to re-test.

Do not change Workshop 1 or the main myworld project.
```

3. Apply the suggested changes in **this folder only**.

## After you fix (expect success)

```bash
docker compose down -v
docker compose up -d
sleep 5
python3 test_connection.py
```

Expected output:

```text
SUCCESS: Connected to Postgres.
```

## Cleanup

```bash
docker compose down -v
```
