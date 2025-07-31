import sqlite3
import os
print("Current working directory:", os.getcwd())
print("Files in this directory:", os.listdir())


connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# ✅ Adding sample data
cur.execute("INSERT INTO bills (customer_name, month, amount) VALUES (?, ?, ?)",
            ('Alice', 'July', 1200.0))

cur.execute("INSERT INTO bills (customer_name, month, amount) VALUES (?, ?, ?)",
            ('Bob', 'June', 950.0))

connection.commit()
connection.close()
