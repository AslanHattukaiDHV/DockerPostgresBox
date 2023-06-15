from database import connect_to_database

# Access the database
conn = connect_to_database()

cur = conn.cursor()

cur.execute("SELECT name, species FROM animals WHERE age>5")


rows = cur.fetchall()
print(rows)

cur.close()
conn.close()