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
            return redirect(url_for('books'))
        else:
            return "Only Admin"
    
    
@app.route('/books')
def books():
    return render_template('books.html')
        

if __name__== "__main__":
    app.run(debug=True)
    

        