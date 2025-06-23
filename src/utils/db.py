import psycopg2
import pandas as pd

def fetch_query_df(sql, conn_str):
    with psycopg2.connect(conn_str) as conn:
        return pd.read_sql(sql, conn)