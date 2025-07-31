import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect('ecommerce.db')  # this will create a file called ecommerce.db
cursor = conn.cursor()

# Create the products table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price REAL,
    stock INTEGER
)
''')

# Save and close
conn.commit()
conn.close()

print("✅ Table created successfully.")
