import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def create_database():

    # Connects to a default database
    # If you intend to run this on your machine you need to make sure the host, dbname, user and password are all valid
    conn = psycopg2.connect("host = 127.0.0.1 dbname=default user=postgres password=phily123")
    conn.set_session(autocommit = True)
    cur = conn.cursor()

    # Creating the new sparkifydb
    # Drop the database to make sure we reset properly
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    # Create sparkify database with UTF8 encoding
    cur.execute("CREATE DATABASE sparkifydb with ENCODING 'utf8' TEMPLATE template0")

    # Close connection to default database
    conn.close()

    # Connect to sparkify database
    conn = psycopg2.connect("host = 127.0.0.1 dbname = sparkifydb user = postgres password = phily123")
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()


