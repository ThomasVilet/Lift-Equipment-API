# Data models for exercises

class Exercise:
    def __init__(self, name, type, category, muscle):
        self.name = name
        self.type = type
        self.category = category
        self.muscle = muscle
        # add more later - maybe instructions/description

    def to_dict(exercise):
        return {
            "_id": str(exercise["_id"]),
            "name": exercise["name"],
            "type": exercise["type"],
            "category": exercise["category"],
            "muscle": exercise["muscle"]
        }
    