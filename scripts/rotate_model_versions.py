import os
import glob

def rotate_versions(version_dir="models/versions", keep_latest=3):
    versions = sorted(
        [d for d in os.listdir(version_dir) if os.path.isdir(os.path.join(version_dir, d))],
        reverse=True
    )
    for old_version in versions[keep_latest:]:
        path = os.path.join(version_dir, old_version)
        print(f"Removing old model version: {path}")
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(path)

if __name__ == "__main__":
    rotate_versions()