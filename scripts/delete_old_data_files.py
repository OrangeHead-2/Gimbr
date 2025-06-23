import os
import glob

def prune_old_files(directory, pattern="*.csv", keep_latest=5):
    files = sorted(
        glob.glob(os.path.join(directory, pattern)),
        key=os.path.getmtime,
        reverse=True
    )
    to_delete = files[keep_latest:]
    for f in to_delete:
        print(f"Deleting old file: {f}")
        os.remove(f)

if __name__ == "__main__":
    prune_old_files("data/raw", "*.csv", keep_latest=5)
    prune_old_files("data/processed", "*.csv", keep_latest=5)