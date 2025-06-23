import pandas as pd
import numpy as np

def add_time_since_last_maintenance(df, date_col='inspection_date', maint_col='last_maintenance_date'):
    df[date_col] = pd.to_datetime(df[date_col])
    df[maint_col] = pd.to_datetime(df[maint_col])
    df['days_since_maintenance'] = (df[date_col] - df[maint_col]).dt.days
    return df

def encode_condition(df, cond_col='bridge_condition'):
    mapping = {
        'Excellent': 4,
        'Good': 3,
        'Fair': 2,
        'Poor': 1,
        'Critical': 0,
    }
    df['cond_encoded'] = df[cond_col].map(mapping).fillna(-1)
    return df

def engineer_features(df):
    df = add_time_since_last_maintenance(df)
    df = encode_condition(df)
    # Add more domain-specific features below
    df['traffic_x_condition'] = df['avg_daily_traffic'] * df['cond_encoded']
    df['is_high_risk'] = ((df['cond_encoded'] <= 1) & (df['avg_daily_traffic'] > 20000)).astype(int)
    return df