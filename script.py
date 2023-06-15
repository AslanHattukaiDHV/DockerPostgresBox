from database import connect_to_database

# Access the database
conn = connect_to_database()

#open cursor
cur = conn.cursor()
cur.execute("SELECT * FROM animals")
rows = cur.fetchall()

if not len(rows):
    print("Empty")
else:
    for row in rows:
        print(row)


cur.close()
conn.close()
