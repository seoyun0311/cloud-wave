import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        database='trip_advisor',
        user='user',
        password='qwer1234'
    )
    return conn