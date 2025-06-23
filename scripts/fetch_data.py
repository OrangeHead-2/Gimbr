import yaml
from src.data.acquisition import DataAcquisition

if __name__ == "__main__":
    with open("config/data_config.yaml") as f:
        config = yaml.safe_load(f)
    da = DataAcquisition(config)
    # Fetch all raw data (full download)
    da.fetch_all()
    print("Data fetch complete.")