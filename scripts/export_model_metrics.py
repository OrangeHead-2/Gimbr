import json

if __name__ == "__main__":
    metrics_path = "models/evaluation/metrics.json"
    output_path = "models/evaluation/metrics_export.csv"
    with open(metrics_path) as f:
        metrics = json.load(f)
    # Flatten metrics for CSV (only top-level for brevity)
    rows = []
    for k, v in metrics.items():
        if isinstance(v, (str, float, int)):
            rows.append((k, v))
    import csv
    with open(output_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["metric", "value"])
        writer.writerows(rows)
    print(f"Exported metrics to {output_path}")