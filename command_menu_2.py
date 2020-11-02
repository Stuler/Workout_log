import sys
from backend import WorkoutLog
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
        self.choices = {
            "1": self.show_workouts,
            "2": self.add_wkout,
            "3": self.modify_workout,
            "4": self.delete_workout,
            "5": self.quit
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
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice.")

    def show_workouts(self):
        pass

    def add_wkout(self):
        wkoutDate = input("Workout date (DD/MM/YYYY): ")
        sport = input("Sport: ")
        wkoutHeader = input("Workout name: ")
        wkoutDesc = input("Description of a workout: ")
        wID = DBase().database.insert_wkout(wkoutDate, sport, wkoutHeader, 
                                            wkoutDesc)
        print (wID)
        Wkout_menu().run()

    def modify_workout(self):
        pass

    def delete_workout(self):
        pass

    def quit(self):
        print("Quitting program")
        sys.exit(0)

class Wkout_menu: 
    def __init__(self):

        self.wkout_choices = {
            "1": self.show_excr,
            "2": self.add_excr,
            "3": self.modify_excr,
            "4": self.delete_excr,
            "5": self.save_wkout
        }

    def add_wkout_menu_display(self):
        print('''
            1. Show excercises
            2. Add new excercise
            3. Modify excercise
            4. Delete excercise
            5. Save and finish workout
        ''')

    def run(self):
        while True:
            self.add_wkout_menu_display()
            choice = input("Enter an option: ")
            action = self.wkout_choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice.")

    def show_excr(self):
        self.excs = self.database.show_excr()
        for excercise in self.excs:
            print (excercise)

    def add_excr(self):
        wID = Menu().add_wkout().wID
        excercise_name = input("Excercise: ")
        excercise_load = input("Excercise load: ")
        reps_done = input("Repeats done: ")
        serie_rpe = input("RPE of an effort: ")
        rest_int = input("Length of rest interval: ")
        note = input("Additional note: ")
        DBase().database.insert_excr(wID, excercise_name, excercise_load, reps_done, 
                                    serie_rpe, rest_int, note)
      
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