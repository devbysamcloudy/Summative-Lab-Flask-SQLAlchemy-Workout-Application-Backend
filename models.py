from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)

    workout_exercises = db.relationship("WorkoutExercise", backref="workout", cascade="all, delete")

    @validates("name")
    def validate_name(self, key, value):
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters")
        return value


class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    category = db.Column(db.String, nullable=False)

    workout_exercises = db.relationship("WorkoutExercise", backref="exercise")

    @validates("category")
    def validate_category(self, key, value):
        if value not in ["strength", "cardio"]:
            raise ValueError("Category must be strength or cardio")
        return value


class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"), nullable=False)

    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)

    __table_args__ = (
        db.CheckConstraint("sets >= 0", name="check_sets_positive"),
    )

    @validates("sets")
    def validate_sets(self, key, value):
        if value is not None and value < 0:
            raise ValueError("Sets must be positive")
        return value