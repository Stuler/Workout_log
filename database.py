import sqlite3

class Database():

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.conn.execute("PRAGMA foreign_keys = 1")

        self.cur_wkout = self.conn.cursor()
        self.cur_excr = self.conn.cursor()

        create_wkout_table =    ('''CREATE TABLE IF NOT EXISTS wkout_lst(
                                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                wkout_date TEXT NOT NULL,
                                sport TEXT NOT NULL,
                                wkout_header TEXT,
                                wkout_desc TEXT
                                );''')
        
        create_excr_table =     ('''CREATE TABLE IF NOT EXISTS excr_lst(
                                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                exc_name TEXT NOT NULL,
                                exc_load REAL NOT NULL,
                                reps_no INTEGER NOT NULL,
                                serie_rpe INTEGER,
                                rest REAL,
                                note TEXT,
                                wkoutId INTEGER NOT NULL,
                                FOREIGN KEY (wkoutId) REFERENCES wkout_lst (id)
                                );''')
        
        print("Successfully connected to SQLite")
        self.cur_wkout.execute(create_wkout_table)
        self.cur_excr.execute(create_excr_table)
        self.conn.commit()
        print("SQLite table created")

    def insert_wkout(self, wkout_date, sport, wkout_header,
                     wkout_desc):
        insert_record = '''INSERT INTO wkout_lst
                            (wkout_date, sport, wkout_header, wkout_desc)
                            VALUES (?,?,?,?);'''
        wkout_data = (wkout_date, sport, wkout_header,
                            wkout_desc)
        self.cur_wkout.execute(insert_record, wkout_data)
        self.conn.commit()
        print("Excercise data inserted successfully into database")

    def insert_excr(self, exc_name, exc_load, reps_no, serie_rpe, rest, 
                            note, wkout_id):
        insert_record = '''INSERT INTO excr_lst
                            (exc_name, exc_load, reps_no, serie_rpe, rest, note,
                            wkoutId)
                            VALUES (?,?,?,?,?,?,?);'''
        excercises_list = (exc_name, exc_load, reps_no, 
                            serie_rpe, rest, note, wkout_id)
        self.cur_excr.execute(insert_record, excercises_list)
        self.conn.commit()
        print("Excercise data inserted successfully into database")

    def show_excr(self):
        show_excr_query = '''SELECT * from excr_lst'''
        self.cur_excr.execute(show_excr_query)
        excercises = self.cur_excr.fetchall()
        return excercises

    def show_added_excr(self, excr_id):
        show_added_query = '''SELECT * from excr_lst'''
        self.cur_excr.execute(show_added_query, ())
        added_excr = self.cur_excr.fetchone()
        print(added_excr, "\n")