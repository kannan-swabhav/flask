import json

def load_db():
    with open('emp_data.json') as f:
        return json.load(f)

db = load_db()