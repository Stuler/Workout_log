import sys
from database import Database

# TODO: add UPDATE functionality on database
# TODO: add SELECT functionality on database

class DBase:
    def __init__(self):
        self.database = Database("workout_log.db")
        self.database.create_tables()

class Menu:
    def __init__(self):
        self.main_choices = {
            "1": self.show_wkouts_run,
            "2": self.add_wkout,
            "3": self.modify_wkout,
            "4": self.delete_wkout,
            "5": self.quit
        }

        self.show_wkouts_choices = {
            "1": self.show_wkouts,
            "2": self.show_last_wkouts,
            "3": self.show_wkout,
            "4": self.rtrn
        }

        self.add_wkout_choices = {
            "1": self.show_excr,
            "2": self.add_excr,
            "3": self.modify_excr,
            "4": self.delete_excr,
            "5": self.rtrn
        }

        self.modify_wkout_choices = {
            "1": self.show_wkouts,
            "2": self.show_last_wkouts,
            "3": self.modify_last_wkout,
            "4": self.modify_wkout,
            "5": self.rtrn
        }

    def display_menu(self):
        print('''
        Workout Log Menu:
        
        1. Show all workouts
        2. Add new workout
        3. Modify workout
        4. Remove workout
        5. Quit 
        ''')

    def show_wkouts_menu(self):
        print('''
            1. Show all workouts
            2. Show last X workouts
            3. Show workout details
            4. Back
        ''')
    
    def add_wkout_menu(self):
        print('''
            1. Show excercises
            2. Add new excercise
            3. Modify excercise
            4. Delete excercise
            5. Back
        ''')

    def modify_wkout_menu(self):
        print('''
            1. Show all workouts
            2. Show last workouts
            3. Modify last workout
            4. Modify particular workout
            5. Back
        ''')

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.main_choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice.")

# Show functionality

    def show_wkouts_run(self):
        while True:
            self.show_wkouts_menu()
            choice = input("Enter an option: ")
            action = self.show_wkouts_choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice.")

    def show_wkouts(self):
        self.wkouts = DBase().database.show_wkouts()
        for wkout in self.wkouts:
            print(f'''
        Workout ID: {wkout[0]}  
                Date: {wkout[1]}    
                Sport: {wkout[2]}
                Name: {wkout[3]}    
                Note: {wkout[4]}
                ''')

    def show_last_wkouts(self):
        self.wkCount = int(input("Number of workouts to show: "))
        self.last_wkouts = DBase().database.show_last_wkouts(self.wkCount)
        print(f"Your last {self.wkCount} workouts: \n")
        for wkout in self.last_wkouts:
                        print(f'''
        Workout ID: {wkout[0]}  
                Date: {wkout[1]}    
                Sport: {wkout[2]}
                Name: {wkout[3]}    
                Note: {wkout[4]}
                ''')

    def show_wkout(self):
        self.wkOut_ID = int(input("Workout ID: "))
        self.wkOut = DBase().database.show_wkout(self.wkOut_ID)
        print(f'''
        Workout ID: {self.wkOut[0]}  
                Date: {self.wkOut[1]}    
                Sport: {self.wkOut[2]}
                Name: {self.wkOut[3]}    
                Note: {self.wkOut[4]}
                ''')

    def show_excr(self):
        self.excs = self.database.show_excr()
        for excercise in self.excs:
            print (excercise)

# Add workout functionality

    def add_wkout(self):
        self.wkOut = DBase().database.insert_wkout(self.getWkoutData())
        self.add_excr_run()

    def getWkoutData(self):
        self.wkoutDate = input("Workout date (DD/MM/YYYY): ")
        self.sport = input("Sport: ")
        self.wkoutHdr = input("Workout name: ")
        self.wkoutDsc = input("Description of a workout: ")
        self.data = (self.wkoutDate, self.sport, self.wkoutHdr, self.wkoutDsc) 
        return(self.data)

# Modify workout functionality

    def modify_last_wkout(self):
        pass

    def modify_wkout(self):
        pass

# Delete functionality

    def delete_wkout(self):
        pass

# Quit

    def quit(self):
        print("Quitting program")
        sys.exit(0)

# Add excercise functionality

    def add_excr_run(self):
        while True:
            self.add_wkout_menu()
            choice = input("Enter an option: ")
            action = self.add_wkout_choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice.")

    def getExcrData(self):
        self.wID = self.wkOut
        self.excr_name = input("Excercise: ")
        self.excr_load = input("Excercise load: ")
        self.reps_done = input("Repeats done: ")
        self.serie_rpe = input("RPE of an effort: ")
        self.rest_int = input("Length of rest interval: ")
        self.note = input("Additional note: ")
        self.data = (self.wID, self.excr_name, self.excr_load, self.reps_done,
                    self.serie_rpe, self.rest_int, self.note)
        return(self.data)

    def add_excr(self):
        DBase().database.insert_excr(self.getExcrData())
      
    def modify_excr(self):
        pass

    def delete_excr(self):
        pass

    def rtrn(self):
        Menu().run()

if __name__ == "__main__":
    Menu().run()