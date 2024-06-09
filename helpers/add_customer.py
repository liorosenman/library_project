import sqlite3

def add_customer():
    name = input("NAME - ")
    city = input("CITY - ")
    age = input("AGE - ")    
    con = sqlite3.connect("library.db")
    cur = con.cursor()
    cur.execute("""
                INSERT INTO customers (name, city, age)
                VALUES (?, ?, ?)
                """, (name, city, age))
    con.commit()
    con.close()
