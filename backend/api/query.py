from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse
import json

from pipelines.generation.generator import mock_stream

router = APIRouter()


@router.get("/query/{run_id}/stream")
async def stream(run_id: str):

    async def event_generator():
        async for event in mock_stream("test query"):
            yield {
                "event": "message",
                "data": json.dumps(event)
            }

    return EventSourceResponse(event_generator())