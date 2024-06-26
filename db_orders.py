from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row
    return conn

def execute_sql_command(sql):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

def get_customers():
    conn = get_db_connection()
    customers = conn.execute('SELECT * FROM customers').fetchall()
    return customers
    # customer_list = [dict(row) for row in customers]
    # return jsonify(customer_list)
   
def get_books():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    return books


