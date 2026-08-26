"""Create a small blogs table and try to insert one row."""

import sqlite3
import sys
from pathlib import Path

from insert_helpers import INSERT_SQL
from models_helpers import BLOG_FIELDS


DB_PATH = Path(__file__).resolve().parent / "drill4.sqlite3"


def create_table(connection: sqlite3.Connection) -> None:
    columns = ", ".join(f"{name} TEXT" for name in BLOG_FIELDS)
    connection.execute(f"DROP TABLE IF EXISTS blogs")
    connection.execute(f"CREATE TABLE blogs ({columns})")
    connection.commit()


def main() -> None:
    connection = sqlite3.connect(DB_PATH)
    try:
        create_table(connection)
        connection.execute(
            INSERT_SQL,
            ("Hello Workshop", "2026-07-15", "10:00:00", "Student"),
        )
        connection.commit()
        row = connection.execute(
            "SELECT title, author FROM blogs LIMIT 1"
        ).fetchone()
    except Exception as exc:
        print("ERROR: insert failed")
        print(exc)
        sys.exit(1)
    finally:
        connection.close()

    print("SUCCESS: Row inserted into blogs table.")
    print(f"title={row[0]} | author={row[1]}")


if __name__ == "__main__":
    main()
