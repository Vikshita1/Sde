import sqlite3

# Connect to the database
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Fetch all rows from the product table
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

# Display the data
for row in rows:
    print(row)

# Close the connection
conn.close()
