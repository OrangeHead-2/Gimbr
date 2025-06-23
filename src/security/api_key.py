import os
from fastapi import Header, HTTPException

def verify_api_key(x_api_key: str = Header(...)):
    expected = os.environ.get("GIMBR_API_KEY")
    if not expected or x_api_key != expected:
        raise HTTPException(status_code=401, detail="Invalid API Key")