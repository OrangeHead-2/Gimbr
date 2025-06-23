def check_column_ranges(df, column, min_val=None, max_val=None):
    if min_val is not None and (df[column] < min_val).any():
        raise ValueError(f"{column} has values below minimum: {min_val}")
    if max_val is not None and (df[column] > max_val).any():
        raise ValueError(f"{column} has values above maximum: {max_val}")

def check_allowed_values(df, column, allowed):
    vals = set(df[column].dropna().unique())
    bad = vals - set(allowed)
    if bad:
        raise ValueError(f"{column} has disallowed values: {bad}")