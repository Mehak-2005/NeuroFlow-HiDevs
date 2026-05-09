# NeuroFlow — Full Observability Stack

## Overview

This task implements a complete observability stack for NeuroFlow including:

- Distributed tracing using OpenTelemetry + Jaeger
- Custom Prometheus metrics
- Grafana dashboards
- Alerting rules with Prometheus
- Monitoring for ingestion, retrieval, generation, and evaluation pipelines

---

# Features Implemented

## Distributed Tracing

Implemented tracing spans for:

### Ingestion
- ingestion.process
- ingestion.extract.{source_type}
- ingestion.chunk
- ingestion.embed
- ingestion.write_db

### Retrieval
- retrieval.pipeline
- retrieval.dense
- retrieval.sparse
- retrieval.metadata
- retrieval.fusion
- retrieval.rerank
- retrieval.assemble

### Generation
- generation.pipeline
- generation.prompt_build
- generation.llm_call
- generation.citation_parse
- generation.log_run

### Evaluation
- evaluation.judge
- evaluation.faithfulness
- evaluation.answer_relevance
- evaluation.context_precision
- evaluation.context_recall

Each span includes:
- pipeline_id
- run_id
- latency
- token count
- chunk count
- model metadata

---

# Prometheus Metrics

Implemented custom metrics inside:

```text
backend/monitoring/metrics.py
```

## Counters
neuroflow_queries_total
neuroflow_ingestion_docs_total
neuroflow_llm_calls_total
neuroflow_circuit_breaker_trips_total

## Histograms
neuroflow_retrieval_latency_seconds
neuroflow_generation_latency_seconds
neuroflow_llm_cost_usd

## Gauges
neuroflow_eval_faithfulness
neuroflow_eval_overall
neuroflow_queue_depth
neuroflow_circuit_breakers_open

---

## Grafana Dashboards

Created dashboards for:

### 1. System Overview
Queries per minute
Retrieval latency
Generation latency
Queue depth
Circuit breaker status
LLM cost

### 2. Quality Monitor
Faithfulness score
Answer relevance
Context precision
Context recall
Overall evaluation trend
Documents ingested

## Alert Rules

Implemented Prometheus alerts:

HighEvaluationFailureRate
CircuitBreakerOpen
EvaluationScoreDegraded
QueueDepthHigh

Located in:
```
infra/prometheus/alerts.yml
```
---
## Tech Stack
FastAPI
OpenTelemetry
Jaeger
Prometheus
Grafana
Docker Compose
PostgreSQL
Redis

---

## Project Structure

```
backend/
│
├── monitoring/
│   ├── metrics.py
│   ├── tracing.py
│   └── __init__.py
│
├── api/
├── pipelines/
└── main.py

infra/
│
├── docker-compose.yml
├── grafana/
└── prometheus/
    ├── prometheus.yml
    └── alerts.yml
```

## Setup Instructions

### 1. Clone Repository
```
git clone <repo-url>
cd NeuroFlow-HiDevs
```
### 2. Start Infrastructure
```
cd infra
docker compose up -d
```
### 3. Start Backend
```
cd ../backend
source venv/Scripts/activate
python -m uvicorn main:app --reload
```

## Service URLs

Service	URL

Backend API	http://127.0.0.1:8000

Metrics	http://127.0.0.1:8000/metrics

Prometheus	http://localhost:9090

Grafana	http://localhost:3001

Jaeger UI	http://localhost:16686

---

## Grafana Login

Username: admin
Password: admin
---
## Verification Checklist

### Metrics

Open:
```
http://127.0.0.1:8000/metrics
```
Verify Prometheus metrics are visible.

### Prometheus

Open:
```
http://localhost:9090
```
Run query:
```
neuroflow_queries_total
```
## Alerts

Open:
```
http://localhost:9090/alerts
```
Verify alert rules are loaded.

## Jaeger Tracing

Open:
```
http://localhost:16686
```
Verify distributed traces:

retrieval.pipeline
generation.pipeline
evaluation.judge

---
## Example Metrics
```
neuroflow_queries_total
neuroflow_retrieval_latency_seconds
neuroflow_generation_latency_seconds
neuroflow_eval_overall
```
--- 

## Docker Services
postgres
redis
prometheus
grafana
jaeger
mlflow

---

## Author

Mehak
---
