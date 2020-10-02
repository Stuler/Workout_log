import sys
from backend import Workout, Excercise, WorkoutLog
from database import Database

class Menu:
    def __init__(self):
        self.log = WorkoutLog()
        self.database = Database("workout_log.db")
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
        Wkout_menu().run()


    def add_exc(self):
        pass

    def modify_workout(self):
        pass

    def delete_workout(self):
        pass

    def quit(self):
        print("Quitting program")
        sys.exit(0)

class Wkout_menu: 
    def __init__(self):
        self.database = Database("workout_log.db")   
        self.wkout_choices = {
            "1": self.add_excr,
            "2": self.show_excr,
            "3": self.modify_excr,
            "4": self.delete_excr,
            "5": self.return_menu
        }

    def add_wkout_menu_display(self):
        print('''
            1. Show excercises
            2. Add new excercise
            3. Modify excercise
            4. Delete excercise
            5. Quit adding excercises / finish workout
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
        pass

    def add_excr(self):
        wkout = "Active"
        while wkout == "Active":
            id = input("Number of an excercise: ")
            excercise_name = input("Excercise: ")
            excercise_load = input("Excercise load: ")
            reps_done = input("Repeats done: ")
            serie_rpe = input("RPE of an effort: ")
            rest_int = input("Length of rest interval: ")
            note = input("Additional note: ")
            self.database.insert_excr(id, excercise_name, excercise_load, 
                                        reps_done, serie_rpe, rest_int, note)
            print("Excercise has been added to the workout!")

    def modify_excr(self):
        pass

    def delete_excr(self):
        pass

    def return_menu(self):
        Menu().run()

if __name__ == "__main__":
    Menu().run()