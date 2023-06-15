from database import connect_to_database
import csv
# Access the database
conn = connect_to_database()

# Specify the file path of the CSV file
csv_file_path = "C:/Users/AslanHattukai/Downloads/avocado.csv"

# Access the database cursor
cur = conn.cursor()

# Create the "avocado" table
create_table_query = """
    CREATE TABLE IF NOT EXISTS avocado (
        "ID" INTEGER,
        "Date" DATE,
        "AveragePrice" FLOAT,
        "TotalVolume" FLOAT,
        "4046" FLOAT,
        "4225" FLOAT,
        "4770" FLOAT,
        "TotalBags" FLOAT,
        "SmallBags" FLOAT,
        "LargeBags" FLOAT,
        "XlargeBags" FLOAT,
        "Type" VARCHAR,
        "Year" INTEGER,
        "Region" VARCHAR
    )
"""
cur.execute(create_table_query)
conn.commit()

# Execute the COPY command to load data from the CSV file
with open(csv_file_path, 'r') as file:
    next(file)
    cur.copy_from(file, 'avocado', sep=',', columns=("ID",
        "Date", "AveragePrice", "TotalVolume", "4046", "4225", "4770",
        "TotalBags", "SmallBags", "LargeBags", "XlargeBags",
        "Type", "Year", "Region"
    ))
conn.commit()

# Now to add a primary key
add_prim_key = "ALTER TABLE avocado ADD avid SERIAL PRIMARY KEY"
cur.execute(add_prim_key)
conn.commit()

cur.close()
conn.close()
