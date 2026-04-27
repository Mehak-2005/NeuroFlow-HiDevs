# API Contracts

## Authentication
- API Key required in headers
- Header: Authorization: Bearer <token>

## Rate Limit
- 100 requests/min per user

---

## POST /ingest

### Request
{
  "source_type": "file|url",
  "data": "file_path_or_url"
}

### Response
{
  "status": "success",
  "document_id": "string"
}

### Errors
- 400: Invalid input
- 500: Processing failed

---

## POST /query

### Request
{
  "query": "string",
  "top_k": 5
}

### Response
{
  "query_id": "string",
  "answer": "string",
  "sources": []
}

---

## GET /query/{query_id}/stream
- SSE stream of tokens

---

## GET /evaluations

### Response
{
  "results": [
    {
      "query": "string",
      "faithfulness": 0.9,
      "relevance": 0.8
    }
  ]
}

---

## GET /evaluations/aggregate

### Response
{
  "avg_faithfulness": 0.85,
  "avg_relevance": 0.82
}

---

## POST /pipelines

### Request
{
  "name": "string",
  "config": {}
}

### Response
{
  "pipeline_id": "string"
}

---

## GET /pipelines/{id}/runs

### Response
{
  "runs": []
}

---

## POST /finetune/jobs

### Request
{
  "dataset": "jsonl_path"
}

### Response
{
  "job_id": "string"
}

---

## GET /finetune/jobs/{id}

### Response
{
  "status": "running|completed"
}

---

## GET /health
### Response
{ "status": "ok" }

---

## GET /metrics
### Response
{ "uptime": "string" }