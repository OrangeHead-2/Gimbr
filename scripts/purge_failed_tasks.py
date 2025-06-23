import redis

if __name__ == "__main__":
    # This script assumes celery backend is Redis and purges failed tasks.
    r = redis.Redis(host="localhost", port=6379, db=1)
    keys = r.keys("celery-task-meta-*")
    purged = 0
    for k in keys:
        data = r.get(k)
        if b'FAILURE' in data:
            r.delete(k)
            purged += 1
    print(f"Purged {purged} failed Celery task results.")