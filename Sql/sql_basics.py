import sqlite3


def db_connect(db_name):
    try:
        conn = sqlite3.connect(f'{db_name}.db')
        return conn
    except sqlite3.Error as e:
        print(e)
    return None


def create_table(conn):
    create_table = """CREATE TABLE IF NOT EXISTS testing (
                                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name TEXT NOT NULL,
                                        email TEXT NOT NULL
                                        );"""
    conn.execute(create_table)


def search_db(conn, column, query):
    cur = conn.cursor()
    cur.execute("SELECT * FROM testing WHERE {}='{}'".format(column, query))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def insert_row(conn, name, email):
    cur = conn.cursor()
    cur.execute("SELECT * FROM testing WHERE name='{}'".format(name))
    if not len(cur.fetchall()):
        conn.execute(
            "INSERT INTO testing (name, email) VALUES (?, ?);", (name, email))
        conn.commit()
    else:
        print('Already exists in db')


if __name__ == "__main__":
    db_name = input("Enter the name of the database you would like to create: ")
    conn = db_connect(db_name)  # connects to db
    create_table(conn)  # creates db in the current directory with given name
    search_db(conn, 'name', 'Harry')  # checks if db has impshum in name column
    insert_row(conn, 'Harry', 'test@test.com')  # adds harry and email to database
