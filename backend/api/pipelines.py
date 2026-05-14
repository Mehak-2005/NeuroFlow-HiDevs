from fastapi import APIRouter

router = APIRouter()


@router.get("/pipelines/{pipeline_id}/runs")
async def get_runs(pipeline_id: str):
    return [{"run_id": "run-123", "latency": 1200, "eval_score": 0.87}]


@router.get("/pipelines/{pipeline_id}/analytics")
async def analytics(pipeline_id: str):
    return {
        "latency": {"p50": 1200, "p95": 1800, "p99": 2200},
        "avg_eval_score": 0.85,
        "cost_per_query": 0.002,
        "queries_last_30_days": [5, 8, 10, 7],
    }
