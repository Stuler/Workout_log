import sqlite3

wkout_id = 0
excr_id = 0

class Database():

    def __init__(self, db):
        self.conn = sqlite3.connect(db)

        create_wkout_table =  ('''CREATE TABLE IF NOT EXISTS wkout_lst(
                                wkout_id INTEGER PRIMARY KEY,
                                workout_date TEXT NOT NULL,
                                sport TEXT NOT NULL,
                                workout_header TEXT NOT NULL,
                                wkout_desc TEXT,
                                );''')
        
        create_excr_table =  ('''CREATE TABLE IF NOT EXISTS excr_lst(
                                excr_id INTEGER PRIMARY KEY,
                                exc_name TEXT NOT NULL,
                                exc_load REAL NOT NULL,
                                reps_no INTEGER NOT NULL,
                                serie_rpe INTEGER,
                                rest REAL,
                                note TEXT
                                );''')
        
        self.cur = self.conn.cursor()
        print("Successfully connected to SQLite")
        self.cur.execute(create_wkout_table)
        self.cur.execute(create_excr_table)
        self.conn.commit()
        print("SQLite table created")

    def insert_wkout(self, wkout_date, sport, wkout_header,
                     wkout_desc):
        self.sport = sport
        self.wkout_header = wkout_header
        self.wkout_desc = wkout_desc
        global wkout_id
        wkout_id += 1
        self.id = wkout_id
        insert_record = '''INSERT INTO wkout_lst
                            (wkout_id, wkout_date, sport, wkout_header,
                                wkout_desc)
                            VALUES (?,?,?,?,?);'''
        wkout_data = (wkout_id, wkout_date, sport, wkout_header,
                            wkout_desc)
        self.cur.execute(insert_record, wkout_data)
        self.conn.commit()
        print("Excercise data inserted successfully into database")



    def insert_excr(self, excr_id, exc_name, exc_load, reps_no, serie_rpe, rest, 
                            note):
        insert_record = '''INSERT INTO excr_lst
                            (excr_id, exc_name, exc_load, reps_no, serie_rpe, 
                            rest, note)
                            VALUES (?,?,?,?,?,?,?);'''
        excercises_list = (excr_id, exc_name, exc_load, reps_no, serie_rpe,
                            rest, note)
        self.cur.execute(insert_record, excercises_list)
        self.conn.commit()
        print("Excercise data inserted successfully into database")

    def show_excr(self):
        show_excr_query = '''SELECT * from excr_lst'''
        self.cur.execute(show_excr_query)
        excercises = self.cur.fetchall()
        return excercises

    def show_added_excr(self, excr_id):
        show_added_query = '''SELECT * from excr_lst where id = ?'''
        self.cur.execute(show_added_query, (excr_id,))
        added_excr = self.cur.fetchone()
        print(added_excr, "\n")