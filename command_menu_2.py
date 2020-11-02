import sys
from database import Database

# TO SOLVE: cursors are recreated each time a workout is added?
# in database.py, get_wkout_id is working, but when called from command_menu,
# cursors are reset

class DBase:
    def __init__(self):
        self.database = Database("workout_log.db")
        self.database.create_tables()

class Menu:
    def __init__(self):
        self.main_choices = {
            "1": self.show_workouts,
            "2": self.add_wkout,
            "3": self.modify_workout,
            "4": self.delete_workout,
            "5": self.quit
        }

        self.add_wkout_choices = {
            "1": self.show_excr,
            "2": self.add_excr,
            "3": self.modify_excr,
            "4": self.delete_excr,
            "5": self.save_wkout
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

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.main_choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice.")

    def show_workouts(self):
        pass

    def getWkoutData(self):
        self.wkoutDate = input("Workout date (DD/MM/YYYY): ")
        self.sport = input("Sport: ")
        self.wkoutHdr = input("Workout name: ")
        self.wkoutDsc = input("Description of a workout: ")
        self.data = (self.wkoutDate, self.sport, self.wkoutHdr, self.wkoutDsc) 
        return(self.data)

    def add_wkout(self):
        self.wkOut = DBase().database.insert_wkout(self.getWkoutData())
        print (self.wkOut)
        self.add_excr_run()

    def modify_workout(self):
        pass

    def delete_workout(self):
        pass

    def quit(self):
        print("Quitting program")
        sys.exit(0)

    def add_wkout_menu_display(self):
        print('''
            1. Show excercises
            2. Add new excercise
            3. Modify excercise
            4. Delete excercise
            5. Save and finish workout
        ''')

    def add_excr_run(self):
        while True:
            self.add_wkout_menu_display()
            choice = input("Enter an option: ")
            action = self.add_wkout_choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice.")

    def show_excr(self):
        self.excs = self.database.show_excr()
        for excercise in self.excs:
            print (excercise)

    def getExcrData(self):
        self.wID = Menu().add_wkout().wkOut
        self.excercise_name = input("Excercise: ")
        self.excercise_load = input("Excercise load: ")
        self.reps_done = input("Repeats done: ")
        self.serie_rpe = input("RPE of an effort: ")
        self.rest_int = input("Length of rest interval: ")
        self.note = input("Additional note: ")

    def add_excr(self):
        DBase().database.insert_excr(self.getExcrData())
      
    def add_excr_menu(self):
        self.excr_menu_choices = {
            "1": self.add_excr,
            "2": self.save_wkout
        }
 
    def add_excr_menu_display(self):
        print('''Excercise has been added to the workout!
                        1. Add another excercise
                        2. Save workout and return to the menu ''')

    def modify_excr(self):
        pass

    def delete_excr(self):
        pass

    def save_wkout(self):
        Menu().run()

if __name__ == "__main__":
    Menu().run()