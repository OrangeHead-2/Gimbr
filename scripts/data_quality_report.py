import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("data/processed/features.csv")
    report = {
        "row_count": len(df),
        "nulls": df.isnull().sum().to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "unique_counts": df.nunique().to_dict(),
        "duplicates": int(df.duplicated().sum()),
        "describe": df.describe().to_dict()
    }
    import json
    with open("data/processed/data_quality_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("Data quality report generated: data/processed/data_quality_report.json")