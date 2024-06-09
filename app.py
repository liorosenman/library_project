from enum import Enum
from helpers.add_customer import add_customer
from helpers.create_db_tables import create_tables
import sqlite3

def login():
    con = sqlite3.connect("library.db")
    cur = con.cursor()
    while True:
        id_to_log = input("What is your ID: ")
        cur.execute(f"SELECT id FROM customers WHERE id = {id_to_log}")
        res = cur.fetchone()
        if res is None:
            print("WRONG ID")
        else:
            if res[0] == 1:
                print("MUST BE FUN")
                user = 1
            else:
                print("HELL YEAH")
                user = 2
            break

def menu():
    choice = int(input("SELECT --- "))
    if (choice == 1):
        add_customer()
        

if(__name__ == "__main__"):
    user = 3
    while True:
        login()
        menu()


            

