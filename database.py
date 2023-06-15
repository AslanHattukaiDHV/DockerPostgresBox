import psycopg2
# this function can be called in scrips that need accest to the database.
def connect_to_database(): 
    conn = psycopg2.connect(
        database="yourdb",
        user="docker",
        password="docker",
        host="127.0.0.1"
    )
    return conn