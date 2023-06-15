from database import connect_to_database

# Access the database
conn = connect_to_database()

cur = conn.cursor()

cur.execute("SELECT avocado.date from avocado WHERE Region = 'Albany'")


rows = cur.fetchall()
print(rows)

cur.close()
conn.close()