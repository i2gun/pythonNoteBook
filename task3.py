import sqlite3 as sl


conn = sl.connect("dec09.db")

cur = conn.cursor()

cur.execute("""
            CREATE TABLE IF NOT EXISTS users
            (
            id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT
            );
            """)

cur.execute("INSERT INTO users VALUES (1,'Ваня','Петров');")
cur.execute("INSERT INTO users VALUES (2,'Сергей','Сергеев');")

cur.execute("SELECT * FROM users;")
print(cur.fetchall())