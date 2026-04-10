from marshmallow import Schema, fields, validates, ValidationError

class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)

    @validates("name")
    def validate_name(self, value):
        if len(value) < 2:
            raise ValidationError("Name too short")


class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    sets = fields.Int()
    reps = fields.Int()

    @validates("sets")
    def validate_sets(self, value):
        if value is not None and value < 0:
            raise ValidationError("Sets must be positive")


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    date = fields.Str(required=True)
    workout_exercises = fields.List(fields.Nested(WorkoutExerciseSchema))