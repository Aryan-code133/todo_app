import json
import os

FILE_PATH = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_PATH) or os.stat(FILE_PATH).st_size == 0:
        return []  # return empty list if file missing or empty
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []  # return empty list if JSON is invalid

def save_tasks(tasks):
    with open(FILE_PATH, "w") as f:
        json.dump(tasks, f, indent=2)
