import joblib
import numpy as np

class ModelEnsemble:
    def __init__(self, model_paths):
        self.models = [joblib.load(p) for p in model_paths]

    def predict_proba(self, X):
        # Average probabilities
        probs = np.array([m.predict_proba(X) for m in self.models])
        return probs.mean(axis=0)