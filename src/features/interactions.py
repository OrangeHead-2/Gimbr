def add_feature_interactions(df):
    # Example: traffic * corrosion, precipitation * avg_temp, etc.
    if "avg_daily_traffic" in df.columns and "corrosion_level" in df.columns:
        df["traffic_corrosion"] = df["avg_daily_traffic"] * df["corrosion_level"]
    if "precipitation" in df.columns and "avg_temp" in df.columns:
        df["rain_heat_index"] = df["precipitation"] * df["avg_temp"]
    return df