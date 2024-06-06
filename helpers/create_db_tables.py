import sqlite3

def create_tables():
    con = sqlite3.connect('library.db')
    cur = con.cursor()
    cur.execute("""
                    CREATE TABLE books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    author TEXT NOT NULL,
                    year_published INTEGER NOT NULL,
                    type INTEGER NOT NULL);
                    """)
    con.commit()
    cur.execute("""
                    CREATE TABLE customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    city TEXT NOT NULL,
                    age INTEGER NOT NULL);
                    """
                    )
    con.commit()
    cur.execute("""
                    CREATE TABLE loans (
                    cust_id INTEGER NOT NULL,
                    book_id INTEGER NOT NULL,
                    loan_date DATE NOT NULL,
                    return_date DATE NOT NULL,
                    FOREIGN KEY (cust_id) REFERENCES customers(id),
                    FOREIGN KEY (book_id) REFERENCES books(id));
                    """)
    con.close()

create_tables()