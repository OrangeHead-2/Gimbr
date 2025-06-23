import pandas as pd
import psycopg2

def fetch_sql_df(sql, conn_str):
    with psycopg2.connect(conn_str) as conn:
        return pd.read_sql(sql, conn)