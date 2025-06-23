import os
import glob
import shutil
from datetime import datetime

def archive_old_files(src_dir="models/evaluation", pattern="*.json", archive_dir="models/archived_evaluations", keep_latest=3):
    os.makedirs(archive_dir, exist_ok=True)
    files = sorted(
        glob.glob(os.path.join(src_dir, pattern)),
        key=os.path.getmtime,
        reverse=True
    )
    for f in files[keep_latest:]:
        base = os.path.basename(f)
        ts = datetime.now().strftime("%Y%m%dT%H%M%S")
        archive_name = f"{ts}_{base}"
        archive_path = os.path.join(archive_dir, archive_name)
        print(f"Archiving {f} to {archive_path}")
        shutil.move(f, archive_path)

if __name__ == "__main__":
    archive_old_files()