import sqlite3

class Database():

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.conn.execute("PRAGMA foreign_keys = ON")
        print("Successfully connected to SQLite")
        self.cur_wkout = self.conn.cursor()
        self.cur_excr = self.conn.cursor()
    
    def create_tables(self):
        create_wkout_table =    ('''CREATE TABLE IF NOT EXISTS wkout_lst(
                                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                wkout_date TEXT NOT NULL,
                                sport TEXT NOT NULL,
                                wkout_header TEXT,
                                wkout_desc TEXT
                                );''')
        self.cur_wkout.execute(create_wkout_table)
        self.conn.commit()
        print("Workout table created")
        
        create_excr_table =     ('''CREATE TABLE IF NOT EXISTS excr_lst(
                                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                wkoutId INTEGER NOT NULL,
                                exc_name TEXT NOT NULL,
                                exc_load REAL NOT NULL,
                                reps_no INTEGER NOT NULL,
                                serie_rpe INTEGER,
                                rest REAL,
                                note TEXT,
                                FOREIGN KEY (wkoutId) REFERENCES wkout_lst (id)
                                );''')
        self.cur_excr.execute(create_excr_table)
        self.conn.commit()
        print("Excercise table created")

    def insert_wkout(self, wkout_data):
        insert_record = '''INSERT INTO wkout_lst
                            (wkout_date, sport, wkout_header, wkout_desc)
                            VALUES (?,?,?,?);'''
        self.cur_wkout.execute(insert_record, wkout_data)
        self.conn.commit()
        print("Workout data inserted successfully into database")
        return self.cur_wkout.lastrowid

    def insert_excr(self,excercises_list):
        insert_record = '''INSERT INTO excr_lst
                            (wkoutId, exc_name, exc_load, reps_no, serie_rpe, 
                            rest, note)
                            VALUES (?,?,?,?,?,?,?);'''
        self.cur_excr.execute(insert_record, excercises_list)
        self.conn.commit()
        print("Excercise data inserted successfully into database")

    def show_wkouts(self):
        show_wkout_query = '''SELECT * from wkout_lst'''
        self.cur_wkout.execute(show_wkout_query)
        wkouts = self.cur_wkout.fetchall()
        return wkouts

    def show_last_wkouts(self, wkOutCount):
        show_wkout_query = '''SELECT * from wkout_lst'''
        self.cur_wkout.execute(show_wkout_query)
        wkouts = self.cur_wkout.fetchmany(wkOutCount)
        print(f"Your last {self.wkOutCount} workouts: \n")
        return wkouts

    def show_wkout_details(self):
        pass

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