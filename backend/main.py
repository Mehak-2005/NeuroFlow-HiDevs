import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from contextlib import asynccontextmanager
import asyncpg
import redis.asyncio as redis
import httpx

from api.ingest import router as ingest_router
from api.query import router as query_router

from config import settings   # make sure config.py exists
from backend.api.compare import router as compare_router

from api.compare import router as compare_router
from api.pipelines import router as pipeline_router



# ---------------- APP INIT ---------------- #

app = FastAPI()

# include routers AFTER app is created
app.include_router(ingest_router)
app.include_router(query_router)
app.include_router(compare_router)
app.include_router(pipeline_router)

# ---------------- GLOBAL CONNECTIONS ---------------- #

pg_pool = None
redis_client = None


# ---------------- LIFESPAN ---------------- #

@asynccontextmanager
async def lifespan(app: FastAPI):
    global pg_pool, redis_client

    # Postgres
    pg_pool = await asyncpg.create_pool(settings.postgres_url)

    # Redis
    redis_client = redis.from_url(settings.redis_url)

    yield

    # Cleanup
    await pg_pool.close()
    await redis_client.close()


app.router.lifespan_context = lifespan


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
            res = await client.get(settings.MLFLOW_URL)
            return res.status_code == 200
    except:
        return False


@app.get("/")
async def root():
    return {"message": "NeuroFlow API working 🚀"}


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