from database import connect_to_database

# Access the database
conn = connect_to_database()

cur = conn.cursor()
cur.execute('SELECT AVG("AveragePrice") as avg_price_region, AVG("TotalVolume") as avg_volume_region, "Region"  FROM avocado GROUP BY "Region" ORDER BY AVG("AveragePrice") DESC LIMIT 10')

rows = cur.fetchall()
print(rows)

cur.close()
conn.close()