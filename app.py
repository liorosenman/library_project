from flask import Flask, render_template
import sqlite3
from helpers import create_db_tables
from flask import Flask, render_template, request, redirect, url_for, session
import db_orders

import sqlite3
con = sqlite3.connect("library.db",check_same_thread=False)
cur = con.cursor()

try:
    cur.execute("CREATE TABLE customers(name,city,age)")
except:
    print("table already exist")

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/customers', methods=['post','get'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        if user_id == '1':
            customers = db_orders.get_customers()
            return render_template('customers.html', customers = customers)
        else:
            return "Only Admin"
    
        

@app.route('/add_customer')
def load_add_customer_page():
    # return 'test'
    return render_template('add_customer.html')

# @app.route('/new_customer_pg')
# def direct_to_new_customer_page():
#     return redirect(url_for('load_add_customer_page'))


@app.route('/new_customer', methods=['GET', 'POST'])
def new_customer():
    print("ERRORRRRRRRRRRRRRRRRRRRRR")
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        age = request.form['age']
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO customers (name, city, age) VALUES (?, ?, ?)', (name, city, age))
        customers = db_orders.get_customers()
        conn.commit()
        conn.close()
        return render_template('customers.html', customers = customers)
    return render_template('customers.html')

@app.route('/upd/<int:id>',methods=['put'])
def upd_user(id):
    data = request.json
    newName = data.get('name')
    newCity = data.get('city')
    newAge = data.get('age')
    sql =f"UPDATE customers SET name = '{newName}', city='{newCity}', age={newAge} WHERE  rowid = {id}"
    cur.execute(sql)
    con.commit()

@app.route('/del/<int:id>', methods = ['delete'])
def del_user(id):
    sql = f"DELETE FROM customers WHERE rowid = {id}"
    cur.execute(sql)
    con.commit()
    
@app.route('/books')
def books():
    return render_template('books.html')
        

if __name__== "__main__":
    app.run(debug=True)
    

        