import jwt
import os
from fastapi import HTTPException

SECRET = os.getenv("SECRET", "YOUR_SECRET")

def encode_jwt(payload):
    return jwt.encode(payload, SECRET, algorithm="HS256")

def decode_jwt(token):
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")