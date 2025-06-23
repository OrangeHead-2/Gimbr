from sklearn.preprocessing import OneHotEncoder

def encode_categoricals(df, categoricals):
    enc = OneHotEncoder(sparse=False, handle_unknown='ignore')
    transformed = enc.fit_transform(df[categoricals])
    # Build DataFrame with new feature names
    feature_names = enc.get_feature_names_out(categoricals)
    df_encoded = pd.DataFrame(transformed, columns=feature_names, index=df.index)
    df = df.drop(columns=categoricals).join(df_encoded)
    return df