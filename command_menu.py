import sys
from backend import Workout, Excercise, WorkoutLog

class Menu:
    def __init__(self):
        self.choices = {
            "1": self.show_workouts,
            "2": self.add_workout,
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
        5. Quit program
        ''')