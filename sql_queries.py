# DROP TABLES

# Drops sparkify database
database_drop = "DROP DATABASE IF EXISTS sparkifydb"
# Creates sparkify database with UTF8 encoding
database_create = "CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0"

# SQL code to drop all tables
songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES & INSERT RECORDS

# SQL code to create and insert into songplay_table
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(songplay_id SERIAL PRIMARY KEY, start_time time NOT NULL, user_id int NOT NULL, level varchar, song_id varchar NOT NULL, artist_id varchar NOT NULL, session_id int,location varchar, user_agent varchar)
""")
songplay_table_insert = ("""INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES( %s, %s, %s, %s, %s, %s, %s, %s)
""")

# SQL code to create and insert into user_table_create
user_table_create = ("""CREATE TABLE IF NOT EXISTS users(user_id int PRIMARY KEY, first_name varchar, last_name varchar, gender varchar, level varchar NOT NULL)
""")
user_table_insert = ("""INSERT INTO users(user_id, first_name, last_name, gender, level) VALUES(%s, %s, %s, %s, %s)
""")

# SQL code to create and insert into  song_table
song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(song_id varchar PRIMARY KEY, title varchar, artist_id varchar NOT NULL, year int, duration decimal)
""")
song_table_insert = ("""INSERT INTO songs(song_id, title, artist_id, year, duration) VALUES(%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

# SQL code to create and insert into  artist_table
artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(artist_id varchar PRIMARY KEY, name varchar, location varchar NOT NULL, lattitude decimal, longitude decimal) 
""")
artist_table_insert = ("""INSERT INTO artists(artist_id, name, location, lattitude, longitude) VALUES(%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

# SQL code to create and insert into  time_table
time_table_create = ("""CREATE TABLE IF NOT EXISTS time(start_time time without time zone PRIMARY KEY, hour int, day int, week int, month int, year int, weekday int)
""")
time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month, year, weekday) VALUES(%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

# FIND SONGS
# Retrieve the artist_id and song_id entries for specific titles, artist name , and song duration.
song_select = (""" SELECT song_id, artists.artist_id FROM songs  LEFT JOIN artists ON songs.artist_id = artists.artist_id WHERE songs.title = (%s) AND artists.name = (%s) AND songs.duration = (%s)
""")

# QUERY LISTS
# Store all the queries into lists (easier imports)
database_reset = [database_drop, database_create]
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]