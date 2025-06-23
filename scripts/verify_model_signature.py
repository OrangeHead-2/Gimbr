import hashlib

def compute_hash(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

if __name__ == "__main__":
    model_path = "models/production/model.joblib"
    signature_path = "models/production/model.joblib.sig"
    computed_hash = compute_hash(model_path)
    if not os.path.exists(signature_path):
        with open(signature_path, "w") as f:
            f.write(computed_hash)
        print(f"Signature created: {signature_path}")
    else:
        with open(signature_path) as f:
            saved_hash = f.read().strip()
        if saved_hash == computed_hash:
            print("Model signature verified: OK")
        else:
            print("WARNING: Model signature mismatch!")