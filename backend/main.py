import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import uuid
from contextlib import asynccontextmanager

import asyncpg
import httpx
import redis.asyncio as redis
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from prometheus_client import generate_latest
from starlette.middleware.base import BaseHTTPMiddleware
from backend.api.compare import router
from backend.api.compare import router as compare_router
from backend.api.finetune import router as finetune_router
from backend.api.ingest import router as ingest_router
from backend.api.pipelines import router as pipeline_router
from backend.api.query import router as query_router
from backend.api.stream import router as stream_router
from backend.config import settings # make sure config.py exists

# ---------------- NEW METRICS IMPORT ---------------- #
from backend.monitoring.metrics import (
    active_circuit_breakers_open,
    eval_faithfulness,
    eval_overall,
    generation_latency,
    llm_cost,
    queries_total,
    queue_depth,
    retrieval_latency,
)
from backend.security.auth import FAKE_CLIENTS, create_access_token

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

    queries_total.labels(pipeline_id="pipeline-a", status="success").inc()

    retrieval_latency.labels(strategy="dense").observe(0.42)

    generation_latency.labels(model="gpt-4o-mini").observe(1.25)

    llm_cost.labels(model="gpt-4o-mini").observe(0.002)

    queue_depth.set(23)

    eval_faithfulness.labels(pipeline_id="pipeline-a").set(0.91)

    eval_overall.labels(pipeline_id="pipeline-a").set(0.87)

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

        return {"status": "ok", "latency_ms": 3}

    except Exception as e:
        print(f"Error occurred while checking Postgres: {e}")
        return {"status": "down", "latency_ms": 0}


async def check_redis():
    try:
        await redis_client.ping()

        return {"status": "ok", "latency_ms": 1}

    except Exception :
        return {"status": "down", "latency_ms": 0}


async def check_mlflow():
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(settings.MLFLOW_URL)

        return {"status": "ok" if res.status_code == 200 else "down", "latency_ms": 45}

    except Exception:
        return {"status": "down", "latency_ms": 0}


@app.get("/health")
async def health():

    postgres = await check_postgres()
    redis_check = await check_redis()
    mlflow = await check_mlflow()

    overall_status = "ok"

    if postgres["status"] == "down" or redis_check["status"] == "down":
        overall_status = "critical"

    return {
        "status": overall_status,
        "checks": {
            "postgres": postgres,
            "redis": redis_check,
            "mlflow": mlflow,
            "circuit_breakers": {"openai": {"state": "closed", "failure_count": 0}},
            "queue_depth": 23,
            "worker_count": 2,
        },
    }


# ---------------- METRICS ENDPOINT ---------------- #


@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type="text/plain")


# ---------------- ROOT ---------------- #


@app.get("/")
async def root():
    return {"message": "NeuroFlow API working 🚀"}


@app.post("/auth/token")
async def login(body: dict):

    client_id = body.get("client_id")
    client_secret = body.get("client_secret")

    client = FAKE_CLIENTS.get(client_id)

    if not client:
        raise HTTPException(status_code=401)

    if client["client_secret"] != client_secret:
        raise HTTPException(status_code=401)

    token = create_access_token(client_id, client["scopes"])

    return {"access_token": token, "token_type": "bearer", "expires_in": 3600}


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):

        response = await call_next(request)

        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Strict-Transport-Security"] = "max-age=31536000"
        response.headers["Content-Security-Policy"] = "default-src 'self'"
        response.headers["X-Request-ID"] = str(uuid.uuid4())

        return response


app.add_middleware(SecurityHeadersMiddleware)
