import subprocess

if __name__ == "__main__":
    # Regenerate requirements.txt from requirements.lock (if using pip-tools)
    result = subprocess.run(["pip-compile", "requirements.lock", "--output-file", "requirements.txt"])
    if result.returncode == 0:
        print("requirements.txt updated from requirements.lock")
    else:
        print("Failed to update requirements.txt")