import sqlite3

class Database():

    def __init__(self, db):
        self.conn = sqlite3.connect(db)

        create_table =  ('''CREATE TABLE IF NOT EXISTS wkout(
                        id INTEGER PRIMARY KEY,
                        workout_date TEXT NOT NULL,
                        sport TEXT NOT NULL,
                        workout_header TEXT NOT NULL,
                        description TEXT,
                        );''')
        
        create_table =  ('''CREATE TABLE IF NOT EXISTS excr_lst(
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

    def insert_excr(self, id, exc_name, exc_load, reps_no, serie_rpe, rest, 
                            note):
        insert_record = '''INSERT INTO excr_lst
                            (id, exc_name, exc_load, reps_no, serie_rpe, rest, 
                            note)
                            VALUES (?,?,?,?,?,?,?);'''
        excercises_list = (id, exc_name, exc_load, reps_no, serie_rpe, rest, 
                            note)
        self.cur.execute(insert_record, excercises_list)
        self.conn.commit()
        print("Python records inserted successfully into database")

    def show_excr(self):
        show_excr_query = '''SELECT * from excr_lst'''
        self.cur.execute(show_excr_query)
        excercises = self.cur.fetchall()
        return excercises
        #for excercise in excercises:
        #    print (f'''{self.id}. {self.exc_name} {self.exc_load} {self.reps_no}
        #           {self.serie_rpe} {self.rest} {self.note}\n''')
        self.cur.close()