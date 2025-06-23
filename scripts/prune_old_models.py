import os
import glob

def keep_latest_n_models(model_dir, n=3):
    models = sorted(glob.glob(os.path.join(model_dir, "model_*.joblib")), reverse=True)
    for old in models[n:]:
        print(f"Removing old model: {old}")
        os.remove(old)

if __name__ == "__main__":
    keep_latest_n_models("models/trained/", n=3)