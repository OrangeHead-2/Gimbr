import yaml
from src.data.acquisition import DataAcquisition

if __name__ == "__main__":
    with open("config/data_config.yaml") as f:
        config = yaml.safe_load(f)
    da = DataAcquisition(config)
    # Fetch only new/updated data
    da.fetch_incremental()
    print("Incremental data fetch complete.")