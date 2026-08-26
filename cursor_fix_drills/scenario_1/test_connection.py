"""Try connecting to Postgres using db_config.py values."""

import sys

import psycopg2

from db_config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER


def main() -> None:
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            connect_timeout=5,
        )
        conn.close()
    except Exception as exc:
        print("ERROR: Could not connect to Postgres.")
        print(exc)
        sys.exit(1)

    print("SUCCESS: Connected to Postgres.")


if __name__ == "__main__":
    main()
