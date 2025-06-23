from datetime import datetime

def parse_date(date_str):
    try:
        return datetime.fromisoformat(date_str)
    except Exception:
        from dateutil.parser import parse
        return parse(date_str)