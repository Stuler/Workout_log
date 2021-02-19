import sys
from database import Database

# TODO: add UPDATE functionality on database
# TODO: refactor menu and choices functions
# TODO: add multiple criterium search functionality
# TODO: incorporate DATETIME 
# TODO: modify printout function for "show all workouts"
# TODO: implement add_set function

class DBase:
    def __init__(self):
        self.database = Database("workout_log.db")
        self.database.create_tables()

class Menu:
    def __init__(self):
        self.main_choices = {
            "1": self.show_wkouts_run,
            "2": self.add_wkout,
            "3": self.modify_wkout_run,
            "4": self.delete_wkout,
            "5": self.quit
        }

        self.show_wkouts_choices = {
            "1": self.show_wkouts,
            "2": self.show_last_wkout,
            "3": self.search_wkout,
            "4": self.show_wkout,
            "5": self.rtrn
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
            "2": self.show_last_wkout,
            "3": self.modify_last_wkout,
            "4": self.modify_part_wkout,
            "5": self.rtrn
        }

        self.search_wkout_choices = {
            "1": self.get_wkout_ID,
            "2": self.get_wkout_DATE,
            "3": self.get_wkout_SPORT,
            "4": self.get_wkout_HDR,
            "5": self.get_wkout_DSC,
            "6": self.rtrn
        }

        self.modify_workout_params = {
            "1": self.modify_wkout_DATE,
            "2": self.modify_wkout_SPORT,
            "3": self.modify_wkout_HDR,
            "4": self.modify_wkout_DSC,
            "5": self.rtrn
        }

    def display_menu(self):
        print('''
            Workout Log Menu:
            
            1. Show workouts
            2. Add new workout
            3. Modify workout
            4. Remove workout
            5. Quit 
        ''')

    def show_wkouts_menu(self):
        print('''
            1. Show all workouts
            2. Show last workout
            3. Search workout
            4. Show workout details
            5. Back
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
            2. Show last workout
            3. Modify last workout
            4. Modify particular workout
            5. Back
        ''')

    def modify_wkout_params_menu(self):
        print('''
            1. Modify workout date
            2. Modify workout sport
            3. Modify workout header
            4. Modify workout description
            5. Edit excercises
            6. Back
            ''')

    def search_menu(self):
        print('''
            1. Search by workout ID
            2. Search by workout date
            3. Search by sport
            4. Search by workout header
            5. Search by workout description
        ''')

# Run the program

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
        for self.wkOut in self.wkouts:
            self.print_wkOut(self.wkOut)

    def show_wkout(self):
        try:
            self.wkOut_ID = self.get_wkout_ID()
            self.wkOut = DBase().database.show_wkout(self.wkOut_ID)
            self.excrs = DBase().database.show_excr(self.wkOut_ID)
            self.print_wkOut(self.wkOut)
            self.print_excrs()
        except TypeError:
            print("Non-existing ID: ", self.wkOut_ID)
  
    def show_last_wkout(self):
        self.last_wkOut = DBase().database.show_last_wkout()
        self.print_wkOut(self.last_wkOut)

    def show_excr(self):
        self.excs = self.database.show_excr()
        for excercise in self.excs:
            print (excercise)

# Search workout

    def search_run(self):
        while True:
            self.search_menu()
            choice = input("Enter an option: ")
            action = self.search_wkout_choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice.")

    def get_wkout_ID(self):
        self.wkout_ID = input("Enter searched ID: ")
        return (self.wkout_ID)

    def get_wkout_DATE(self):
        self.wkout_DATE = input("Enter date of a workout: ")
        return (self.wkout_DATE)

    def get_wkout_SPORT(self):
        self.wkout_SPORT = input("Enter searched sport: ")
        return (self.wkout_SPORT)

    def get_wkout_HDR(self):
        self.wkout_HDR = input("Enter workout header: ")
        return (self.wkout_HDR)

    def get_wkout_DSC(self):
        self.wkout_DSC = input("Enter workout description: ")
        return (self.wkout_DSC)

    def search_wkout(self):      
        self.wkouts = DBase().database.search_wkout(
            self.get_wkout_ID(),
            self.get_wkout_DATE(),
            self.get_wkout_SPORT(),
            self.get_wkout_HDR(),
            self.get_wkout_DSC()        
            )
        self.print_wkOuts(self.wkouts)

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

    def modify_wkout_run(self):
        while True:
            self.modify_wkout_menu()
            choice = input("Enter an option: ")
            action = self.modify_wkout_choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice.")

    def modify_wkout(self):
        pass
  
    def modify_part_wkout(self):
        self.id = self.get_wkout_ID()
        self.date = self.get_wkout_DATE()
        self.sport = self.get_wkout_SPORT()
        self.header = self.get_wkout_HDR()
        self.desc = self.get_wkout_DSC()
        DBase().database.modify_wkout(self.date, self.sport, 
                            self.header, self.desc, self.id)

    def modify_last_wkout(self):
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

# Print out functions

    def print_wkOut(self, wkOut):
        print(f'''
            Workout ID:     {wkOut[0]}  
                    Date:   {wkOut[1]}    
                    Sport:  {wkOut[2]}
                    Name:   {wkOut[3]}    
                    Note:   {wkOut[4]}
                    ''')

    def print_wkOuts(self, wkOuts):
        self.wkOuts_lst = list(enumerate(wkOuts, start=1))
        print(f"{'ID':6}{'DATE':16}{'SPORT':20}{'NAME':20}{'DESCRIPTION'}") 
        print(80*"*")
        for i in self.wkOuts_lst:
            print(f"{i[1][0]!s:6}{i[1][1]:16}{i[1][2]:20}{i[1][3]:20}{i[1][4]}")

    def print_excrs(self):
        self.exc_lst = list(enumerate(self.excrs, start=1))
        for i in self.exc_lst:
            print(f'''
            Exc no.: {i[0]}
                        Exc. name:          {i[1][2]}    
                        Load:               {i[1][3]}
                        Number of reps:     {i[1][4]}    
                        RPE:                {i[1][5]}
                        Rest interval:      {i[1][6]}
                        Additional note:    {i[1][7]}
                ''')
    
if __name__ == "__main__":
    Menu().run()