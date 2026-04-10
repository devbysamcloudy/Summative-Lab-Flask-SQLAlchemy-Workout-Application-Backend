from flask import Flask, request, jsonify
from models import db, Workout, Exercise, WorkoutExercise
from schemas import WorkoutSchema, ExerciseSchema, WorkoutExerciseSchema
from flask_migrate import Migrate


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)


workout_schema = WorkoutSchema()
exercise_schema = ExerciseSchema()
we_schema = WorkoutExerciseSchema()



@app.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()
    return jsonify(workout_schema.dump(workouts, many=True))


@app.route("/workouts", methods=["POST"])
def create_workout():
    data = request.get_json()
    try:
        workout = Workout(**data)
        db.session.add(workout)
        db.session.commit()
        return workout_schema.dump(workout), 201
    except Exception as e:
        return {"error": str(e)}, 400


@app.route("/workouts/<int:id>", methods=["DELETE"])
def delete_workout(id):
    workout = Workout.query.get(id)
    if not workout:
        return {"error": "Workout not found"}, 404

    db.session.delete(workout)
    db.session.commit()
    return {"message": "Deleted"}, 200


@app.route("/exercises", methods=["GET"])
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify(exercise_schema.dump(exercises, many=True))


@app.route("/exercises", methods=["POST"])
def create_exercise():
    data = request.get_json()
    try:
        exercise = Exercise(**data)
        db.session.add(exercise)
        db.session.commit()
        return exercise_schema.dump(exercise), 201
    except Exception as e:
        return {"error": str(e)}, 400


@app.route("/exercises/<int:id>", methods=["DELETE"])
def delete_exercise(id):
    exercise = Exercise.query.get(id)
    if not exercise:
        return {"error": "Exercise not found"}, 404

    db.session.delete(exercise)
    db.session.commit()
    return {"message": "Deleted"}, 200


@app.route("/workout_exercises", methods=["POST"])
def add_exercise():
    data = request.get_json()
    try:
        we = WorkoutExercise(**data)
        db.session.add(we)
        db.session.commit()
        return we_schema.dump(we), 201
    except Exception as e:
        return {"error": str(e)}, 400


if __name__ == "__main__":
    app.run(debug=True)