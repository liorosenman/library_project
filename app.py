from flask import Flask, render_template
import sqlite3
from helpers import create_db_tables
from flask import Flask, render_template, request, redirect, url_for, session
import db_orders
from ObjectsModules.user_types import book_types 
import sqlite3

# con = sqlite3.connect("library.db",check_same_thread=False)
# cur = con.cursor()

try:
    sql = "CREATE TABLE customers(name,city,age)"
    db_orders.execute_sql_command(sql)
    # cur.execute("CREATE TABLE customers(name,city,age)")
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
     

@app.route('/new_customer', methods=['GET', 'POST'])
def new_customer():
    # print("ERRORRRRRRRRRRRRRRRRRRRRR")
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        age = request.form['age']
        sql = f"INSERT INTO customers (name, city, age) VALUES ('{name}','{city}',{age})"
        db_orders.execute_sql_command(sql)
        # conn = sqlite3.connect('library.db')
        # cursor = conn.cursor()
        # cursor.execute('INSERT INTO customers (name, city, age) VALUES (?, ?, ?)', (name, city, age))
        customers = db_orders.get_customers()
        # conn.commit()
        # conn.close()
        return render_template('customers.html', customers = customers)
    return render_template('customers.html')

@app.route('/upduser/<int:id>',methods=['put'])
def upd_user(id):
    data = request.json
    newName = data.get('name')
    newCity = data.get('city')
    newAge = data.get('age')
    sql =f"UPDATE customers SET name = '{newName}', city='{newCity}', age={newAge} WHERE  id = {id}"
    db_orders.execute_sql_command(sql)
    # cur.execute(sql)
    # con.commit()

@app.route('/deluser/<int:id>', methods = ['delete'])
def del_user(id):
    sql = f"DELETE FROM customers WHERE id = {id}"
    db_orders.execute_sql_command(sql)
    # cur.execute(sql)
    # con.commit()
    
@app.route('/books')
def books():
    books = db_orders.get_books()
    return render_template('books.html', book_types = book_types, books = books)

@app.route('/new_book', methods=['GET', 'POST'])
def new_book():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        year_published = request.form['year_published']
        book_type = request.form['book_type']
        sql = f"INSERT INTO books (name, author, year_published, type) VALUES ('{name}', '{author}', {year_published}, {book_type})"
        db_orders.execute_sql_command(sql)
        # conn = sqlite3.connect('library.db')
        # cursor = conn.cursor()
        # cursor.execute('INSERT INTO books (name, author, year_published, type) VALUES (?, ?, ?, ?)',
        #                 (name, author, year_published, book_type))
        books = db_orders.get_books()
        # conn.commit()
        # conn.close()
        return render_template('books.html', book_types = book_types,  books = books)
    return render_template('books.html')

@app.route('/updbook/<int:id>', methods=['put'])

def upd_book(id):
    print("THE UPDATE HAS TO WORK!!!")
    data = request.json
    print(data)
    name = data.get('name')
    print(name)
    author = data.get('author')
    print(author)
    year = data.get('year')
    print(year)
    type = data.get('type')
    print(type)
    sql = f"UPDATE books SET name = '{name}', author='{author}', year_published={year}, type = {type} WHERE id = {id}"
    db_orders.execute_sql_command(sql)

@app.route('/delbook/<int:id>', methods = ['delete'])
def del_book(id):
    con = sqlite3.connect("library.db",check_same_thread=False)
    cur = con.cursor()
    print(f'THE ID FOR DELETION IS {id}')
    sql = f"DELETE FROM books WHERE id = {id}"
    cur.execute(sql)
    con.commit()
    con.close()
        
if __name__== "__main__":
    app.run(debug=True)
    

        