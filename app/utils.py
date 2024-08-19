# Helper functions and validation 
from flask import jsonify
from bson import ObjectId

# check if a string is a valid ObjectId
def is_valid_objectid(id_str):
    return ObjectId.is_valid(id_str)

# create a standardized JSON response
def create_response(data=None, message="", status=200):
    response = {
        "status": status,
        "message": message,
        "data": data
    }
    return jsonify(response), status

# handle a 404 error
def not_found(message="Resource not found"):
    return create_response(message=message, status=404)
