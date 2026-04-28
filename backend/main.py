from fastapi import FastAPI
import asyncpg
import redis.asyncio as redis
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API working"}

@app.get("/health")
async def health():
    checks = {"postgres": False, "redis": False, "mlflow": True}

    try:
        conn = await asyncpg.connect(
            user="neuroflow",
            password=os.getenv("POSTGRES_PASSWORD"),
            database="neuroflow",
            host="127.0.0.1",
            port=5432
        )
        await conn.execute("SELECT 1")
        await conn.close()
        checks["postgres"] = True
    except Exception as e:
        print("Postgres error:", e)

    try:
        r = redis.Redis(
            host="127.0.0.1",
            port=6379,
            password=os.getenv("REDIS_PASSWORD"),
            decode_responses=True
        )
        await r.ping()
        checks["redis"] = True
    except Exception as e:
        print("Redis error:", e)

    return {
        "status": "ok" if all(checks.values()) else "error",
        "checks": checks
    }