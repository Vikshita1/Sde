import sqlite3

conn = sqlite3.connect('products.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL
    )
''')

# Insert sample products
products = [
    ('Laptop', 'A powerful laptop', 1000),
    ('Smartphone', 'A new smartphone', 700),
    ('Headphones', 'Noise cancelling', 150),
    ('Monitor', '24-inch Full HD', 200)
]

cursor.executemany('INSERT INTO products (name, description, price) VALUES (?, ?, ?)', products)

conn.commit()
conn.close()
