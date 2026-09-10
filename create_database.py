import sqlite3
import pandas as pd

# Load cleaned CSV
df = pd.read_csv("Cleaned_Amazon_Sales.csv")

# Check columns
print("Columns in cleaned data:")
print(df.columns.tolist())

# Connect to SQLite database
conn = sqlite3.connect("amazon_sales.db")

# Replace old table with updated data
df.to_sql("amazon_sales", conn, if_exists="replace", index=False)

# Check total records
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM amazon_sales")

print("Total records:", cursor.fetchone()[0])
print("Database updated successfully!")

conn.close()