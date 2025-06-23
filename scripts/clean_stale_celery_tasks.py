import redis
import json

def clean_stale_tasks(redis_host="localhost", redis_port=6379, db=1, hours_stale=12):
    r = redis.Redis(host=redis_host, port=redis_port, db=db)
    keys = r.keys("celery-task-meta-*")
    purged = 0
    import time
    threshold = time.time() - hours_stale * 3600
    for k in keys:
        task_meta = json.loads(r.get(k))
        # Celery task metadata includes 'date_done' ISO8601 string
        date_done = task_meta.get("date_done")
        if date_done:
            from dateutil.parser import parse
            completed = parse(date_done).timestamp()
            if completed < threshold:
                r.delete(k)
                purged += 1
    print(f"Purged {purged} stale Celery tasks.")

if __name__ == "__main__":
    clean_stale_tasks()