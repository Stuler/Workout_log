import datetime

class Workout:
    '''Represents a workout in a logbook.'''

    def __init__(self, sport, workout_header):
        self.workout_date = datetime.date.today()
        self.sport = sport 
        self.workout_header = workout_header
        self.excercises = []

    def add_excercise(self, ex):
        self.excercises.append(Excercise)

class Excercise:
    '''Represents a particular excercise done during workout.'''

    def __init__(self, excercise_name, excercise_load, reps_done, serie_rpe,
    rest_int, note):
        self.excercise_name = excercise_name
        self.excercise_load = excercise_load
        self.reps_done = reps_done
        self.serie_rpe = serie_rpe
        self.rest_int = rest_int
        self.note = note

class WorkoutLog:
    '''Represents a logbook of workouts done by user.'''

    def __init__(self):
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(Workout)

    def show_workout(self):
        pass

#log = WorkoutLog()
#workout = Workout("Fitness", "Push workout")
#excercise = Excercise("Dumbell press", 35, 6, 8, 2.5, "Felt good")
#workout.add_excercise(excercise)
#log.add_workout(workout)