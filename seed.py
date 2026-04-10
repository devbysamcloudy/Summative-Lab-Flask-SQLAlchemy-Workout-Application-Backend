from app import app
from models import db, Workout, Exercise, WorkoutExercise

with app.app_context():
    db.drop_all()
    db.create_all()

    w1 = Workout(name="Morning Workout", date="2026-04-10")
    e1 = Exercise(name="Push Ups", category="strength")
    e2 = Exercise(name="Jogging", category="cardio")

    db.session.add_all([w1, e1, e2])
    db.session.commit()

    we1 = WorkoutExercise(workout_id=w1.id, exercise_id=e1.id, sets=3, reps=12)

    db.session.add(we1)
    db.session.commit()

    print("Database seeded!")