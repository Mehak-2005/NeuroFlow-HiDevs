from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse
import json

from pipelines.generation.generator import mock_stream

from fastapi import APIRouter

router = APIRouter()

ratings = {}

@router.patch("/runs/{run_id}/rating")
async def rate_run(run_id: str, body: dict):
    ratings[run_id] = body["rating"]
    return {"status": "saved", "run_id": run_id}


@router.get("/query/{run_id}/stream")
async def stream(run_id: str):

    async def event_generator():
        async for event in mock_stream("test query"):
            yield {
                "event": "message",
                "data": json.dumps(event)
            }

    return EventSourceResponse(event_generator())