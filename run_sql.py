import sqlite3

conn = sqlite3.connect("amazon_sales.db")
cursor = conn.cursor()

with open("queries.sql", "r") as file:
    query = file.read()

cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(row)

conn.close()