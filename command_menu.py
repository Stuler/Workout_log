import sys
from backend import Workout, Excercise, WorkoutLog
from database import Database

class Menu:
    def __init__(self):
        self.log = WorkoutLog()
        self.database = Database("workout_log.db")
        self.choices = {
            "1": self.show_workouts,
            "2": self.add_wkout_menu,
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

    def add_wkout_menu(self):
        self.wkout_choices = {
            "1": 
        }

    def add_wkout_menu_display(self):
        print('''
            1. Add new excercise
            2. Modify excercise
            3. Quit adding excercises / finish workout
        ''')

    def add_wkout(self):
        wkout = "Active"
        while wkout == "Active":
            prompt = input("")
            id = input("Number of an excercise: ")
            excercise_name = input("Excercise: ")
            excercise_load = input("Excercise load: ")
            reps_done = input("Repeats done: ")
            serie_rpe = input("RPE of an effort: ")
            rest_int = input("Length of rest interval: ")
            note = input("Additional note: ")
            self.database.insert_workout(id, excercise_name, excercise_load, 
                                        reps_done, serie_rpe, rest_int, note)
            print("Excercise has been added to the workout!")

    def add_exc(self):
        pass

    def modify_workout(self):
        pass

    def delete_workout(self):
        pass

    def quit(self):
        print("Quitting program")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()