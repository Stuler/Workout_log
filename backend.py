import datetime

class Workout:
    '''Represents a workout in a logbook.'''
    workouts = []

    def __init__(self, sport, workout_header, description):
        self.workout_date = datetime.date.today()
        self.sport = sport 
        self.workout_header = workout_header
        self.description = description
        self.excercises = []
        Workout.workouts.append(self)

    def add_excercise(self, excercise_name, excercise_load, 
    reps_done, serie_rpe, rest_int, note):
        self.excercises.append(Excercise(excercise_name, excercise_load, 
        reps_done, serie_rpe, rest_int, note))

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

    def add_workout(self):
        self.workouts.append(Workout)

log = WorkoutLog()
workout = Workout("Fitness","Push day", "Focused on squats")
workout.add_excercise("Dumpbell press", 35, 6, 8, 2.5, "Felt good")
workout.add_excercise("Squats", 92.5, 4, 9, 3.5, "Felt really hard, good slow" 
" technique")

print(workout.workouts[0].excercises[1].excercise_name)