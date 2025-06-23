import pandas as pd
from sklearn.preprocessing import LabelEncoder

def feature_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    # Example: encode region_code, create interaction, time since maintenance, cluster
    if "region_code" in df.columns:
        le = LabelEncoder()
        df["region_cluster"] = le.fit_transform(df["region_code"].astype(str))
    if "avg_daily_traffic" in df.columns and "corrosion_level" in df.columns:
        df["traffic_x_corrosion"] = df["avg_daily_traffic"] * df["corrosion_level"]
    if "inspection_date" in df.columns and "last_maintenance_date" in df.columns:
        df["days_since_maintenance"] = (pd.to_datetime(df["inspection_date"]) - pd.to_datetime(df["last_maintenance_date"])).dt.days
    return df