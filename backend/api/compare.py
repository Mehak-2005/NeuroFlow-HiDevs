from fastapi import APIRouter
import asyncio
import uuid
import random
import time

router = APIRouter()

async def run_pipeline(name: str):
    start = time.time()

    await asyncio.sleep(1.5)

    retrieval_latency = 500
    total_latency = int((time.time() - start) * 1000)

    run_id = str(uuid.uuid4())

    # simulate evaluation trigger
    await asyncio.sleep(0.1)

    return {
        "run_id": run_id,
        "generation": f"[{name}] Answer for: What is AI?",
        "retrieval_latency_ms": retrieval_latency,
        "total_latency_ms": total_latency,
        "chunks_used": 5,
        "eval_score": round(random.uniform(0.8, 0.95), 2)
    }

@router.post("/pipelines/compare")
async def compare_pipelines(data: dict):

    query = data["query"]

    pipeline_a, pipeline_b = await asyncio.gather(
        run_pipeline("A"),
        run_pipeline("B")
    )

    return {
        "query": query,
        "pipeline_a": pipeline_a,
        "pipeline_b": pipeline_b
    }