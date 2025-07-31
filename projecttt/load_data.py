import sqlite3
import pandas as pd

# Read the CSV file
df = pd.read_csv('products.csv')  # Make sure the CSV file is in the same folder

# Connect to the existing database
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Load data into the 'products' table
df.to_sql('products', conn, if_exists='replace', index=False)

# Save and close
conn.commit()
conn.close()

print("✅ Data loaded into the database successfully.")
