from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import FastAPI

limiter = Limiter(key_func=get_remote_address)

def register_rate_limit(app: FastAPI):
    app.state.limiter = limiter