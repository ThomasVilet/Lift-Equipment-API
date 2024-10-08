# API routes/endpoints
from flask import Blueprint, jsonify, request
from .database import exercises
from .utils import is_valid_objectid, create_response
from .services import get_exercise_by_id, get_all_exercises, get_exercise_list_by_field, get_filtered_exercises

api = Blueprint('api', __name__)

@api.route('/api/exercise', methods=['GET'])
def get_gen_exercises():
    name = request.args.get('name')
    type = request.args.get('type')
    category = request.args.get('category')
    muscle = request.args.get('muscle')
    try:
        exercise_list = get_filtered_exercises(name, type, category, muscle)
        return create_response(data=exercise_list, message="Exercises retrieved successfully")
    except ValueError as e:
        return create_response(message=str(e), status=400)

@api.route('/api/exercises', methods=['GET'])
def get_exercises():
    try: 
        exercise_list = get_all_exercises()
        return create_response(data=exercise_list, message="Exercises retrieved successfully")
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

@api.route('/api/exercises/name=<input>', methods=['GET'])
def get_exercises_by_name(input):
    try:
        exercise_list = get_exercise_list_by_field('name', input)
        return create_response(data=exercise_list, message="Exercises retrieved successfully")
    except ValueError as e:
        return create_response(message=str(e), status=400)

@api.route('/api/exercises/type=<input>', methods=['GET'])
def get_exercises_by_type(input):
    try:
        exercise_list = get_exercise_list_by_field('type', input)
        return create_response(data=exercise_list, message="Exercises retrieved successfully")
    except ValueError as e:
        return create_response(message=str(e), status=400)

@api.route('/api/exercises/category=<input>', methods=['GET'])
def get_exercises_by_category(input):
    try:
        exercise_list = get_exercise_list_by_field('category', input)
        return create_response(data=exercise_list, message="Exercises retrieved successfully")
    except ValueError as e:
        return create_response(message=str(e), status=400)

@api.route('/api/exercises/muscle=<input>', methods=['GET'])
def get_exercises_by_muscle(input):
    try:
        exercise_list = get_exercise_list_by_field('muscle', input)
        return create_response(data=exercise_list, message="Exercises retrieved successfully")
    except ValueError as e:
        return create_response(message=str(e), status=400)
    
    # Add insert, update, and delete // add functionality for user to play test (radio button), make display one div instead of 4 different - FRIDAY GOAL

    # Authentication will be needed later when starting Villa (name thought)