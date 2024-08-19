# Lift Equipment API
 This application will contain a library of lifting equipment and exercises that third parties can access. The reason for creating this program was because all other workout APIs did not allow me to add or update exercises. I found myself more frustrated that I could not find the exercise I was looking for, so I took it into my own hands. I am using this API for another application that allows users to join gym communities and post their various workouts for others to see.

## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the application
    ```bash
    python main.py
    ```

## Directory Structure
- `models.py`: Data models for exercises
- `routes.py`: API routes/endpoints
- `services.py`: Business logic for handling exercise data
- `database.py`: MongoDB connection and configuration
- `utils.py`: Helper functions and data validation
- `main.py`: Runs the application