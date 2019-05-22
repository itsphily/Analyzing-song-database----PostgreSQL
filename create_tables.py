import psycopg2
from sql_queries import create_table_queries, drop_table_queries, database_reset


def create_database():
    # connect to default database
    conn = psycopg2.connect("host = 127.0.0.1 dbname=default user=postgres password=phily123")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # Drops and creates a sparkify database with UTF8 encoding
    for query in database_reset:
        cur.execute(query)
        conn.commit()

    # close connection to default database
    conn.close()

    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
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
