from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse
import asyncio

router = APIRouter()

@router.get("/query/{run_id}/stream")
async def stream_query(run_id: str):

    async def event_generator():

        words = [
            "Artificial",
            " intelligence",
            " is",
            " the",
            " simulation",
            " of",
            " human",
            " intelligence."
        ]

        for word in words:
            yield {"data": word}
            await asyncio.sleep(0.4)

    return EventSourceResponse(event_generator())