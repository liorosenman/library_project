from flask import Flask, render_template
import sqlite3
from helpers import create_db_tables
from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def login_post():
    if request.method == 'POST':
        user_id = request.form['user_id']
        if user_id == '1':
            # return redirect(url_for('customers'), user_id = user_id)
            return render_template('customers.html', user_id = user_id)
        else:
            return "Only Admin"

@app.route('/customers')
def customers():
     user_id = request.args.get('user_id')
     return render_template('customers.html', user_id = user_id) 

@app.route('/add_customer_page')
def to_add_customer_page():
    return render_template('add_customer.html') 

@app.route('/new_customer', methods=['GET', 'POST'])
def new_customer():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        age = request.form['age']
        conn = sqlite3.connect('customers.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO customers (name, city, age) VALUES (?, ?, ?)', (name, city, age))
        conn.commit()
        conn.close()
        return render_template('customers.html')
    return render_template('add_customer.html')
    
@app.route('/books')
def books():
    return render_template('books.html')
        

if __name__== "__main__":
    app.run(debug=True)
    

        