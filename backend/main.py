from fastapi import FastAPI
from contextlib import asynccontextmanager
import asyncpg
import redis.asyncio as redis
import httpx
from api.ingest import router as ingest_router

# ✅ TEMP settings (since config not used)
POSTGRES_URL = "postgresql://neuroflow:postgres123@localhost:5432/neuroflow"
REDIS_URL = "redis://:redis123@localhost:6379"
MLFLOW_URL = "http://localhost:5000"

# Global connections
pg_pool = None
redis_client = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global pg_pool, redis_client

    # Connect Postgres
    pg_pool = await asyncpg.create_pool(POSTGRES_URL)

    # Connect Redis
    redis_client = redis.from_url(REDIS_URL)

    yield

    # Cleanup
    await pg_pool.close()
    await redis_client.close()


# ✅ CREATE app FIRST
app = FastAPI(lifespan=lifespan)

# ✅ THEN include router
app.include_router(ingest_router)


# ---------------- HEALTH CHECK ---------------- #

async def check_postgres():
    try:
        async with pg_pool.acquire() as conn:
            await conn.execute("SELECT 1")
        return True
    except:
        return False


async def check_redis():
    try:
        await redis_client.ping()
        return True
    except:
        return False


async def check_mlflow():
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(MLFLOW_URL)
            return res.status_code == 200
    except:
        return False


@app.get("/")
def root():
    return {"message": "API working"}


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "checks": {
            "postgres": await check_postgres(),
            "redis": await check_redis(),
            "mlflow": await check_mlflow(),
        },
    }