from monitoring.tracing import tracer
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

        with tracer.start_as_current_span("retrieval.pipeline") as span:
            span.set_attribute("run_id", run_id)
            span.set_attribute("pipeline_id", "pipeline-a")

            yield {
                "event": "message",
                "data": json.dumps({
                    "type": "retrieval_start"
                })
            }

        with tracer.start_as_current_span("generation.pipeline") as span:
            span.set_attribute("run_id", run_id)
            span.set_attribute("pipeline_id", "pipeline-a")

            async for event in mock_stream("test query"):
                yield {
                    "event": "message",
                    "data": json.dumps(event)
                }

        with tracer.start_as_current_span("evaluation.judge") as span:
            span.set_attribute("run_id", run_id)
            span.set_attribute("pipeline_id", "pipeline-a")
            span.set_attribute("faithfulness", 0.91)
            span.set_attribute("answer_relevance", 0.88)

            yield {
                "event": "message",
                "data": json.dumps({
                    "type": "evaluation_complete",
                    "faithfulness": 0.91,
                    "answer_relevance": 0.88
                })
            }

    return EventSourceResponse(event_generator())