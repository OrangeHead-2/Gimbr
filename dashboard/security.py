from fastapi import Request, HTTPException
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter

# In api.py
@app.on_event("startup")
async def startup():
    import aioredis
    redis = await aioredis.create_redis_pool("redis://localhost")
    await FastAPILimiter.init(redis)

@app.post("/predict", dependencies=[Depends(RateLimiter(times=10, seconds=60))])
def predict(data: list, user=Depends(verify_jwt)):
    # as before
    ...