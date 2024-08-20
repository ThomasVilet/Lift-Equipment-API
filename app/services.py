# Business logic for handling exercise data
from .database import exercises
from .models import Exercise
from bson.objectid import ObjectId


# validate exercise and prepare exercise data
def validate_exercise_data(data):
    required_fields = ["name", "type", "category", "muscle"]
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")
    return data

# testing purposes
def get_random_exercise():
    exercise = exercises.find_one()
    if exercise:
        return Exercise.to_dict(exercise)
    else:
        raise ValueError("Exercise not found")

# Service function to fetch all exercises
def get_all_exercises():
    exercise_list = [Exercise.to_dict(exercise) for exercise in exercises.find()]
    return exercise_list

# Service function to fetch a single exercise by ID - usually used to alter its data
def get_exercise_by_id(exercise_id):
    exercise = exercises.find_one({"_id": ObjectId(exercise_id)})
    if exercise:
        return Exercise.to_dict(exercise)
    else:
        raise ValueError("Exercise not found")
    
def get_exercise_list_by_input(passed_input):
    exercise_list = [Exercise.to_dict(exercise) for exercise in exercises.find({
        "$text": {"$search": passed_input}
    }).limit(10)]
    if exercise_list:
        return exercise_list
    else: 
        raise ValueError("Input Invalid; Exercises not found")
    
# ---------------------- Fix all under this line -------------------------------------------

# Service function to add a new exercise - Only admins should have access to this
def add_exercise(data):
    validated_data = validate_exercise_data(data)
    exercise_id = exercises.insert_one(validated_data).inserted_id
    return str(exercise_id)

# Service function to update an existing exercise - Only admins should have access to this
def update_exercise(exercise_id, data):
    validated_data = validate_exercise_data(data)
    result = exercises.update_one({"_id": ObjectId(exercise_id)}, {"$set": validated_data})
    if result.modified_count == 1:
        return True
    else:
        raise ValueError("Failed to update exercise or no changes made")

# Service function to delete an exercise
def delete_exercise(exercise_id):
    result = exercises.delete_one({"_id": ObjectId(exercise_id)})
    if result.deleted_count == 1:
        return True
    else:
        raise ValueError("Exercise not found or could not be deleted")
