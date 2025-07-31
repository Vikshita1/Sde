import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# Create the 'products' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT
    )
''')

# Insert sample products
products = [
    ('Shampoo', 120.50, 'Cleans and softens hair'),
    ('Toothpaste', 75.00, 'Minty fresh toothpaste'),
    ('Face Wash', 150.00, 'Oil control face wash'),
    ('Body Lotion', 230.00, 'Moisturizing body lotion')
]

cursor.executemany('INSERT INTO products (name, price, description) VALUES (?, ?, ?)', products)

conn.commit()
conn.close()

print("✅ Database initialized with sample products.")
