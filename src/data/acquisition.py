import pandas as pd
import os
import shutil

class DataAcquisition:
    def __init__(self, config):
        self.config = config

    def fetch_all(self):
        # Example: fetch from local demo file
        if "raw_path" in self.config and "demo_file" in self.config:
            shutil.copy2(self.config["demo_file"], self.config["raw_path"])

    def fetch_incremental(self):
        # Simulate incremental fetch
        if "raw_path" in self.config and "demo_file" in self.config:
            target = self.config["raw_path"].replace(".csv", "_new.csv")
            shutil.copy2(self.config["demo_file"], target)

    def fetch_weather(self, weather_url, out_path):
        # Example: download weather data from a CSV URL
        weather_df = pd.read_csv(weather_url)
        weather_df.to_csv(out_path, index=False)

    def fetch_inspections(self, inspection_url, out_path):
        # Example: download inspection data from a CSV URL
        insp_df = pd.read_csv(inspection_url)
        insp_df.to_csv(out_path, index=False)