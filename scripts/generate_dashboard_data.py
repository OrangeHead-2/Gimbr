import pandas as pd

if __name__ == "__main__":
    # This script prepares the data file needed for the dashboard/app.py map and summary views.
    # It expects features and predictions to be available.
    features_file = "data/processed/features.csv"
    model_file = "models/trained/model.joblib"
    output_file = "models/evaluation/predictions.csv"

    import joblib
    from src.features.engineering import feature_pipeline

    df = pd.read_csv(features_file)
    if "failure_probability" not in df.columns:
        model = joblib.load(model_file)
        features = [c for c in df.columns if c not in ['structure_id', 'failure_within_1yr', 'failure_probability']]
        df['failure_probability'] = model.predict_proba(df[features])[:, 1]
    if "region_cluster" not in df.columns:
        df = feature_pipeline(df)  # ensure region_cluster is present

    # Save only necessary columns for the dashboard
    dashboard_cols = ['structure_id', 'latitude', 'longitude', 'failure_probability', 'region_cluster']
    dashboard_df = df[dashboard_cols]
    dashboard_df.to_csv(output_file, index=False)
    print(f"Dashboard data generated at {output_file}")