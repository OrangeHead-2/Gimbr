import os

def ensure_dir_exists(path):
    os.makedirs(path, exist_ok=True)