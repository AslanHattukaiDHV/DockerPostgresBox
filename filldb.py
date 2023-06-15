from database import connect_to_database

# Access the database
conn = connect_to_database()

cur = conn.cursor()
sql ="INSERT INTO animals (name, species, age) VALUES(%s, %s, %s)"
data =[
    ("hans", "frog", "2"),
    ("anke", "turtle", "200"),
    ("arie", "bee", "1"),
    ("ben", "bear", "6"),
    ("greet", "gorilla", "18"),
    ("dana", "elephant", "30"),
    ("lien", "lion", "10"),
    ("hanna", "goat", "12")
]
cur.executemany(sql,data)
conn.commit()
cur.close()
conn.close()