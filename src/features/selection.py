from sklearn.feature_selection import SelectKBest, f_classif

def select_top_features(X, y, k=10):
    selector = SelectKBest(f_classif, k=k)
    selector.fit(X, y)
    support = selector.get_support(indices=True)
    return X.iloc[:, support]