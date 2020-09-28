import sqlite3

try:
    conn = sqlite3.connect("log_database.db")
    sqlite_create_table_query = '''CREATE TABLE workout_data(
                                id INTEGER PRIMARY KEY,
                                exc_name TEXT NOT NULL,
                                exc_load REAL NOT NULL,
                                reps_no INTEGER,
                                serie_rpe INTEGER,
                                note TEXT
                                );'''

    cur = conn.cursor()
    print("Successfully connected to SQLite")
    cur.execute(sqlite_create_table_query)
    conn.commit()
    print("SQLite table created")

    cur.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (conn):
        conn.close()
        print("The SQLite connection is closed")

def insert_workout(id, exc, exc_load, reps_no, serie_rpe, note):
    try:
        conn = sqlite3.connect("log_database.db")
        cur = conn.cursor()
        print("Successfully connected to SQLite")

        insert_serie = '''INSERT INTO workout_data
                        (id, exc, exc_load, reps_no, serie_rpe, note)
                        VALUES (?,?,?,?,?,?);'''
        data_set = (id, exc, exc_load, reps_no, serie_rpe, note)
        cur.execute(insert_serie, data_set)
        conn.commit()
        print("Python variables inserted successfully into database")
        cur.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")
