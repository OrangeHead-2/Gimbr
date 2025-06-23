from sklearn.decomposition import PCA
import pandas as pd

def add_pca_features(df, feature_cols, n_components=2, prefix="pca"):
    pca = PCA(n_components=n_components)
    components = pca.fit_transform(df[feature_cols].fillna(0))
    for i in range(n_components):
        df[f"{prefix}_{i+1}"] = components[:, i]
    return df