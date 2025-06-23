import psycopg2
import os

def refresh_views():
    db_url = os.environ.get("POSTGRES_URL")
    if not db_url:
        print("Set POSTGRES_URL environment variable.")
        return
    with psycopg2.connect(db_url) as conn:
        with conn.cursor() as cur:
            cur.execute("REFRESH MATERIALIZED VIEW CONCURRENTLY infra_summary_mv;")
            print("Refreshed materialized view: infra_summary_mv")
            cur.execute("REFRESH MATERIALIZED VIEW CONCURRENTLY region_stats_mv;")
            print("Refreshed materialized view: region_stats_mv")

if __name__ == "__main__":
    refresh_views()