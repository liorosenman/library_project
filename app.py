from flask import Flask, render_template
import sqlite3
from helpers import create_db_tables

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
    try:
        create_db_tables.create_tables()
    except:
        print("---Tables exist---")

        