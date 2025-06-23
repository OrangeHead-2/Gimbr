import shutil
import os

if __name__ == "__main__":
    cache_dirs = ["__pycache__", ".cache", "data/cache"]
    for d in cache_dirs:
        if os.path.exists(d):
            try:
                shutil.rmtree(d)
                print(f"Cleared cache: {d}")
            except Exception as e:
                print(f"Could not clear {d}: {e}")