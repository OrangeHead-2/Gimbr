import tempfile
import shutil

if __name__ == "__main__":
    tempdir = tempfile.gettempdir()
    for prefix in ["gimbr_", "tmp"]:
        for sub in os.listdir(tempdir):
            path = os.path.join(tempdir, sub)
            if os.path.isdir(path) and sub.startswith(prefix):
                try:
                    shutil.rmtree(path)
                    print(f"Removed temp directory: {path}")
                except Exception as e:
                    print(f"Could not remove {path}: {e}")