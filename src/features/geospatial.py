import pandas as pd
from geopy.distance import geodesic

def add_nearest_city_distance(df, ref_points):
    # ref_points: list of (lat, lon)
    def min_dist(row):
        here = (row["latitude"], row["longitude"])
        return min(geodesic(here, city).km for city in ref_points)
    if "latitude" in df.columns and "longitude" in df.columns:
        df["dist_to_city_km"] = df.apply(min_dist, axis=1)
    return df