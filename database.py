import sqlite3

class Database():

    def __init__(self, db):
            self.conn = sqlite3.connect(db)
            
            create_table =  ('''CREATE TABLE IF NOT EXISTS workout_data(
                                        id INTEGER PRIMARY KEY,
                                        exc_name TEXT NOT NULL,
                                        exc_load REAL NOT NULL,
                                        reps_no INTEGER NOT NULL,
                                        serie_rpe INTEGER,
                                        rest REAL,
                                        note TEXT
                                        );''')
            
            self.cur = self.conn.cursor()
            print("Successfully connected to SQLite")
            self.cur.execute(create_table)
            self.conn.commit()
            print("SQLite table created")

    def insert_workout(self, id, exc_name, exc_load, reps_no, serie_rpe, rest, 
                            note):
            insert_record = '''INSERT INTO workout_data
                            (id, exc_name, exc_load, reps_no, serie_rpe, rest, 
                            note)
                            VALUES (?,?,?,?,?,?,?);'''
            excercises_list = (id, exc_name, exc_load, reps_no, serie_rpe, rest, 
                            note)
            self.cur.execute(insert_record, excercises_list)
            self.conn.commit()
            print("Python records inserted successfully into database")
