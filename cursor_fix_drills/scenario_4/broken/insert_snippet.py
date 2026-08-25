# BUG for drill: column/field name typo "titel" instead of "title"
sql = """INSERT INTO members_blog (titel, release_date, blog_time, author, created_date)
         VALUES (%s, %s::DATE, %s::TIME, %s, NOW())"""

def add_row_to_blog(curs, title, author, date, time):
    curs.execute(sql, (title, date, time, author))
