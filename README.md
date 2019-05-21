# Creating Postgres database
The goal is to create a Postgres database with tables designed to optimize queries on song play analysis.


# My role
Create a database schema and ETL pipeline for the song play analysis.


# Database schema
## Defined fact and dimension tables
###fact table: songplays
the fact table was meant to store records in log data associated with song plays.
The fields include: start_time, user_id, level, song_id, artist_id, session_id,location, user_agent
The fact table has been designed to answer the question what songs are users listening to.
###dimension tables: users, songs, artists, time

# ETL pipeline
Transfers data from files in two local directories into the previously defined fact and dimension tables using Python and SQL


# Scripts and notebooks included
## create_tables.py
Creates the sparkify database and resets the tables (drops and creates them)
## etl.ipynb
Performs the ETL (step by step) on a single song file and load a single record into each table
Performs the ETL on a single file of the log_data to create the time and users dimensional tables as well as the songplays fact table
## SQL_queries.py
Script to drop (to reset), and create the tables we will use in our defined schema. In addition, the script includes the insert SQL statements required to fill the tables using the values from the logs.


# Some questions to which answers are queries optimized with this schema
Most listened to songs per country
Number of users per country
Most listened to free/paid songs or artists
Most listened to free/paid songs or artists per country
Average of free/paid songs per users
