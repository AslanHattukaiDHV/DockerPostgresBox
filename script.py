from database import connect_to_database

# Access the database
conn = connect_to_database()

#open cursor
cur = conn.cursor()
cur.execute("SELECT * FROM avocado")
rows = cur.fetchall()

if not len(rows):
    print("Empty")
else:
    rownr =len(rows)
    print (rownr)


cur.close()
conn.close()
