from database import connect_to_database

# Access the database
conn = connect_to_database()

#open cursor
cur = conn.cursor()
cur.execute("SELECT * FROM avocado")
rows = cur.fetchall()
first_row = cur.fetchone()

if not len(rows):
    print("Empty")

else:
    print (first_row)
    
cur.close()
conn.close()
