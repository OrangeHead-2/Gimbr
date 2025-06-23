import json

def load_json(path):
    with open(path) as f:
        return json.load(f)

def save_json(obj, path):
    import os
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)