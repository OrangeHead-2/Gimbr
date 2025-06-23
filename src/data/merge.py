import pandas as pd

def merge_dataframes(df_main, df_weather=None, df_inspections=None, on="structure_id"):
    """Merge main data with optional weather and inspection dataframes."""
    if df_weather is not None:
        df_main = pd.merge(df_main, df_weather, on=on, how="left", suffixes=("", "_weather"))
    if df_inspections is not None:
        df_main = pd.merge(df_main, df_inspections, on=on, how="left", suffixes=("", "_insp"))
    return df_main