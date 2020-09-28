import sqlite3

def insert_workout(id, exc, exc_load, reps_no, serie_rpe, note):
    try:
        conn = sqlite3.connect("log_database.db")
        cur = conn.cursor()
        print("Successfully connected to SQLite")

        insert_serie = ('''INSERT INTO )
