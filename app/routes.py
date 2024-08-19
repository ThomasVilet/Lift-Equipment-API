# API routes/endpoints
from flask import Blueprint, jsonify, request
from .database import exercises
from .utils import is_valid_objectid, create_response
from .services import get_exercise_by_id, get_random_exercise, get_all_exercises

api = Blueprint('api', __name__)

# test
@api.route('/api/exercise', methods=['GET'])
def get_random_api_exercise():
    try:
        exercise = get_random_exercise()
        # return exercise
        return create_response(data=exercise, message="Exercise retrieved successfully")
    except ValueError as e:
        return create_response(message=str(e), status=400)

@api.route('/api/exercises', methods=['GET'])
def get_exercises():
    try: 
        exercise_list = get_all_exercises()
        return create_response(data=exercise_list, message="Exercise retrieved successfully")
    except ValueError as e:
        return create_response(message=str(e), status=400)
    
@api.route('/api/num-exercises', methods=['GET'])
def get_num_exercises():
    try: 
        exercise_list = get_all_exercises()
        exercise_num = len(exercise_list)
        return create_response(data=exercise_num, message="Exercise retrieved successfully")
    except ValueError as e:
        return create_response(message=str(e), status=400)

@api.route('/api/exercises/<id>', methods=['GET'])
def get_exercise(id):
    if not is_valid_objectid(id):
        return create_response(message="Invalid Id format", status=400)
    try:
        exercise = get_exercise_by_id(id)
        return create_response(data=exercise, message="Exercise retrieved successfully")
    except ValueError as e:
        return create_response(message=str(e), status=400)
