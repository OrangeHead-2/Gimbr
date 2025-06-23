import matplotlib.pyplot as plt

def plot_feature_importance(importances, feature_names, out_file="feature_importance.png"):
    plt.figure(figsize=(10, 5))
    sorted_idx = importances.argsort()[::-1]
    plt.bar(range(len(importances)), importances[sorted_idx])
    plt.xticks(range(len(importances)), [feature_names[i] for i in sorted_idx], rotation=90)
    plt.tight_layout()
    plt.savefig(out_file)
    plt.close()