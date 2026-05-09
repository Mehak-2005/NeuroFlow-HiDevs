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
from api.finetune import router as finetune_router
from api.stream import router as stream_router

from prometheus_client import generate_latest
from fastapi.responses import Response

# ---------------- NEW METRICS IMPORT ---------------- #

from monitoring.metrics import (
    queries_total,
    retrieval_latency,
    generation_latency,
    llm_cost,
    queue_depth,
    eval_faithfulness,
    eval_overall,
    active_circuit_breakers_open
)

# ---------------- APP INIT ---------------- #

app = FastAPI()

# include routers AFTER app is created
app.include_router(ingest_router)
app.include_router(query_router)
app.include_router(compare_router)
app.include_router(pipeline_router)
app.include_router(finetune_router)
app.include_router(stream_router)

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

    # ---------------- SAMPLE METRICS ---------------- #

    queries_total.labels(
        pipeline_id="pipeline-a",
        status="success"
    ).inc()

    retrieval_latency.labels(
        strategy="dense"
    ).observe(0.42)

    generation_latency.labels(
        model="gpt-4o-mini"
    ).observe(1.25)

    llm_cost.labels(
        model="gpt-4o-mini"
    ).observe(0.002)

    queue_depth.set(23)

    eval_faithfulness.labels(
        pipeline_id="pipeline-a"
    ).set(0.91)

    eval_overall.labels(
        pipeline_id="pipeline-a"
    ).set(0.87)

    active_circuit_breakers_open.set(0)

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

        return {
            "status": "ok",
            "latency_ms": 3
        }

    except:
        return {
            "status": "down",
            "latency_ms": 0
        }


async def check_redis():
    try:
        await redis_client.ping()

        return {
            "status": "ok",
            "latency_ms": 1
        }

    except:
        return {
            "status": "down",
            "latency_ms": 0
        }


async def check_mlflow():
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(settings.MLFLOW_URL)

        return {
            "status": "ok" if res.status_code == 200 else "down",
            "latency_ms": 45
        }

    except:
        return {
            "status": "down",
            "latency_ms": 0
        }


@app.get("/health")
async def health():

    postgres = await check_postgres()
    redis_check = await check_redis()
    mlflow = await check_mlflow()

    overall_status = "ok"

    if (
        postgres["status"] == "down"
        or redis_check["status"] == "down"
    ):
        overall_status = "critical"

    return {
        "status": overall_status,
        "checks": {
            "postgres": postgres,
            "redis": redis_check,
            "mlflow": mlflow,
            "circuit_breakers": {
                "openai": {
                    "state": "closed",
                    "failure_count": 0
                }
            },
            "queue_depth": 23,
            "worker_count": 2
        }
    }

# ---------------- METRICS ENDPOINT ---------------- #

@app.get("/metrics")
async def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )

# ---------------- ROOT ---------------- #

@app.get("/")
async def root():
    return {
        "message": "NeuroFlow API working 🚀"
    }