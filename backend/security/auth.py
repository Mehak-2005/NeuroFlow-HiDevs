from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = "neuroflow-secret"
ALGORITHM = "HS256"

security = HTTPBearer()

FAKE_CLIENTS = {
    "admin-client": {
        "client_secret": "admin123",
        "scopes": ["query", "ingest", "admin"]
    },
    "query-client": {
        "client_secret": "query123",
        "scopes": ["query"]
    }
}

def create_access_token(client_id: str, scopes: list):
    expire = datetime.utcnow() + timedelta(hours=1)

    payload = {
        "sub": client_id,
        "scopes": scopes,
        "exp": expire
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    return verify_token(token)

def require_scope(scope: str):
    def checker(user=Depends(get_current_user)):
        if scope not in user["scopes"]:
            raise HTTPException(
                status_code=403,
                detail="Insufficient scope"
            )
        return user

    return checker