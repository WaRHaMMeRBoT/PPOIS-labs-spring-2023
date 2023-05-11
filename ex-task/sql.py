import sqlite3

conn = sqlite3.connect("base.db")
cursor = conn.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    email TEXT,
    phoneNumber TEXT
)"""
)

conn.commit()


def register(user_name, user_email, user_number):
    cursor.execute(f"SELECT name FROM users WHERE name = '{user_name}'")
    if cursor.fetchone() is None:
        cursor.execute(
            f"INSERT INTO users VALUES (?,?,?)", (user_name, user_email, user_number)
        )
        conn.commit()
    else:
        print("Already exists")

    for value in cursor.execute("SELECT * FROM users"):
        print(value)


def delete(user_name="", user_email="", user_number=""):
    cursor.execute(f"DELETE FROM users WHERE name = '{user_name}'")
    cursor.execute(f"DELETE FROM users WHERE email = '{user_email}'")
    cursor.execute(f"DELETE FROM users WHERE phoneNumber = '{user_number}'")
    conn.commit()


def getBase():
    base = []
    for value in cursor.execute("SELECT * FROM users"):
        base.append(value)
    return base
