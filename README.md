# Workout API

## Project Description
This project is a backend API built using Flask, Flask-SQLAlchemy, and Marshmallow.  
It allows personal trainers to create workouts, manage exercises, and assign exercises to workouts.

Each workout can have multiple exercises, and exercises can be reused across different workouts.  
Additional details like sets and reps can be stored when linking an exercise to a workout.

---

## Technologies Used
- Python
- Flask
- Flask-SQLAlchemy
- Marshmallow

---

## Installation Instructions

1. Clone the repository:
   git clone <https://github.com/devbysamcloudy/Summative-Lab-Flask-SQLAlchemy-Workout-Application-Backend>

2. Navigate into the project folder:
   cd workout-api

3. Create a virtual environment:
   python -m venv venv

4. Activate the environment:
   venv\Scripts\activate

5. Install dependencies:
   pip install -r requirements.txt

---

## Setting Up the Database

1. Initialize the migration repository:
   flask db init

2. Generate the migration script:
   flask db migrate -m "initial migration"

3. Apply the migrations to create the database:
   flask db upgrade

---

## Running the Application

Start the server by running:
python app.py

The app will run on:
http://127.0.0.1:5000/

---

## Seeding the Database

To create sample data, run:
python seed.py

---

## API Endpoints

### Workouts
- GET /workouts  
  Returns all workouts  

- POST /workouts  
  Creates a new workout  

- DELETE /workouts/<id>  
  Deletes a workout  

---

### Exercises
- GET /exercises  
  Returns all exercises  

- POST /exercises  
  Creates a new exercise  

- DELETE /exercises/<id>  
  Deletes an exercise  

---

### Workout Exercises
- POST /workout_exercises  
  Adds an exercise to a workout with sets and reps  

---

## Example Request

POST /workouts

{
  "name": "Leg Day",
  "date": "2026-04-10"
}

---

## Notes
- The API does not include update routes as per the requirements.
- Validations are implemented at the model, schema, and database level.
- Exercises are reusable across multiple workouts.

---

## Author
- GitHub: [devbysamcloudy](https://github.com/devbysamcloudy/Summative-Lab-Flask-SQLAlchemy-Workout-Application-Backend)
- Email: snganga685@gmail.com

---

## License
This project is licensed under the [MIT License](LICENSE).