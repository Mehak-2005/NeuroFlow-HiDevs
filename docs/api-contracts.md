# API Contracts

## POST /ingest
Request:
{ "source": "file/url" }

Response:
{ "status": "success" }

## POST /query
Request:
{ "query": "string" }

Response:
{ "answer": "string" }

## GET /query/{id}/stream
SSE stream

## GET /evaluations
Paginated list

## GET /evaluations/aggregate
Metrics summary

## POST /pipelines
Create pipeline

## GET /pipelines/{id}/runs
Run history

## POST /finetune/jobs
Start job

## GET /finetune/jobs/{id}
Status

## GET /health
## GET /metrics