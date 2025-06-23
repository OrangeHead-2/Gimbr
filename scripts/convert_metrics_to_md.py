import json

if __name__ == "__main__":
    in_path = "models/evaluation/metrics.json"
    out_path = "models/evaluation/metrics.md"
    with open(in_path) as f:
        metrics = json.load(f)
    with open(out_path, "w") as f:
        f.write("# Model Metrics\n\n")
        for k, v in metrics.items():
            if isinstance(v, dict):
                f.write(f"## {k}\n")
                for subk, subv in v.items():
                    f.write(f"- {subk}: {subv}\n")
                f.write("\n")
            else:
                f.write(f"- **{k}**: {v}\n")
    print(f"Metrics exported to {out_path}")