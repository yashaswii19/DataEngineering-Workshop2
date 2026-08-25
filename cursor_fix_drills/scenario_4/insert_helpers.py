"""SQL used when inserting a blog row."""

# Column list must match models_helpers.BLOG_FIELDS / the real table.
INSERT_SQL = """
INSERT INTO blogs (titel, release_date, blog_time, author, created_date)
VALUES (?, ?, ?, ?, datetime('now'))
"""
