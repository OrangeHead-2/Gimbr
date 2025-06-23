import joblib
from sklearn.ensemble import RandomForestClassifier
import os

def train_model(df, model_cfg, model_dir):
    features = [c for c in df.columns if c not in ['structure_id', 'failure_within_1yr']]
    X = df[features]
    y = df['failure_within_1yr']
    clf = RandomForestClassifier(**model_cfg.get("rf_params", {}))
    clf.fit(X, y)
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(clf, os.path.join(model_dir, "model.joblib"))
    return clf

def drift_detection(new_df, ref_df, features):
    # KS test for drift
    from scipy.stats import ks_2samp
    drift = {}
    for f in features:
        if f in new_df.columns and f in ref_df.columns:
            stat, pval = ks_2samp(ref_df[f].dropna(), new_df[f].dropna())
            drift[f] = {"ks_stat": float(stat), "p_value": float(pval)}
    return drift