# Configuration and connection for MongoDB
from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://tvilet3:{password}@exerciseinformation.1gntk.mongodb.net/?retryWrites=true&w=majority&appName=ExerciseInformation"
client = MongoClient(connection_string)

db = client['Exercises']
exercises = db['Exercises'] # Collection with the data

exercises.create_index([('name', 'text'),
                        ('type', 'text'),
                        ('category', 'text'),
                        ('muscle', 'text')])
