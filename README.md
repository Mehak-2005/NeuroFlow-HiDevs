# 🚀 NeuroFlow — Task 8  
# Named Pipeline System — Config-Driven RAG with A/B Comparison

---

# 📌 Overview

This task implements a configurable Named Pipeline System for NeuroFlow.  
The system allows different Retrieval-Augmented Generation (RAG) pipelines to be defined using structured JSON configurations instead of hardcoded logic.

The implementation supports:

- Named pipeline configurations
- Strict schema validation using Pydantic
- Pipeline versioning
- Parallel A/B pipeline comparison
- Pipeline analytics
- Pipeline run history
- Evaluation score tracking
- Async execution using `asyncio.gather`

This enables multiple RAG strategies to be tested and compared without changing application code.

---

# 🎯 Objectives Achieved

✅ Config-driven pipeline architecture  
✅ Strict validation with Pydantic  
✅ Named and versioned pipelines  
✅ A/B comparison endpoint  
✅ Parallel pipeline execution  
✅ Pipeline analytics endpoint  
✅ Pipeline run history endpoint  
✅ Evaluation score integration  
✅ Async processing using FastAPI + asyncio  

---

# 🏗 Project Structure

```text
backend/
│
├── api/
│   ├── compare.py
│   ├── pipelines.py
│
├── models/
│   ├── __init__.py
│   ├── pipeline.py
│
├── main.py
```

---

# ⚙️ Pipeline Configuration Schema

Implemented using Pydantic models in:

```text
backend/models/pipeline.py
```

The schema supports four major sections:

## 1️⃣ Ingestion Configuration

Controls:
- chunking strategy
- chunk size
- overlap
- extractor configuration

Example:

```json
{
  "chunking_strategy": "hierarchical",
  "chunk_size_tokens": 400,
  "chunk_overlap_tokens": 80,
  "extractors_enabled": ["pdf", "docx"]
}
```

---

## 2️⃣ Retrieval Configuration

Controls:
- dense retrieval
- sparse retrieval
- reranking
- metadata filtering
- query expansion

Example:

```json
{
  "dense_k": 30,
  "sparse_k": 20,
  "reranker": "cross-encoder",
  "top_k_after_rerank": 8,
  "query_expansion": true,
  "metadata_filters_enabled": true
}
```

---

## 3️⃣ Generation Configuration

Controls:
- model routing
- context window
- temperature
- prompt style

Example:

```json
{
  "max_context_tokens": 6000,
  "temperature": 0.2,
  "system_prompt_variant": "precise"
}
```

---

## 4️⃣ Evaluation Configuration

Controls:
- automatic evaluation
- training thresholds

Example:

```json
{
  "auto_evaluate": true,
  "training_threshold": 0.82
}
```

---

# 🔒 Strict Validation

The pipeline schema rejects unknown keys using:

```python
ConfigDict(extra="forbid")
```

This guarantees:
- schema consistency
- safer pipeline configuration
- prevention of invalid configuration injection

---

# 🔀 A/B Pipeline Comparison

Implemented endpoint:

```text
POST /pipelines/compare
```

This endpoint:
- accepts a query
- runs two pipelines simultaneously
- compares outputs side-by-side

---

# ⚡ Parallel Execution

Pipelines are executed concurrently using:

```python
asyncio.gather()
```

This reduces overall latency and ensures:
- faster response time
- efficient async execution
- real-time comparison capability

---

# 📊 Response Format

The compare endpoint returns:

```json
{
  "query": "What is AI?",
  "pipeline_a": {
    "run_id": "uuid",
    "generation": "response",
    "retrieval_latency_ms": 505,
    "total_latency_ms": 1510,
    "chunks_used": 5,
    "eval_score": 0.85
  },
  "pipeline_b": {
    "run_id": "uuid",
    "generation": "response",
    "retrieval_latency_ms": 510,
    "total_latency_ms": 1520,
    "chunks_used": 5,
    "eval_score": 0.80
  }
}
```

---

# 📈 Analytics Endpoint

Implemented:

```text
GET /pipelines/{id}/analytics
```

Provides:
- p50 latency
- p95 latency
- p99 latency
- average evaluation score
- query trends
- estimated cost per query

Example response:

```json
{
  "latency": {
    "p50": 1200,
    "p95": 1800,
    "p99": 2200
  },
  "avg_eval_score": 0.85,
  "cost_per_query": 0.002
}
```

---

# 📜 Pipeline Run History

Implemented:

```text
GET /pipelines/{id}/runs
```

Tracks:
- run IDs
- latency
- evaluation scores
- pipeline executions

---

# 🧠 Evaluation Trigger

After comparison execution:
- asynchronous evaluation jobs are triggered
- evaluation scores are generated
- pipeline quality metrics are updated

---

# 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| FastAPI | Backend API framework |
| asyncio | Parallel execution |
| Pydantic | Schema validation |
| Docker | Containerization |
| PostgreSQL | Data storage |
| Redis | Caching |
| Uvicorn | ASGI server |

---

# ▶️ Run Instructions

## 1️⃣ Start Docker Services

```bash
cd infra
docker compose up -d
```

---

## 2️⃣ Verify Running Containers

```bash
docker ps
```

Expected containers:

- infra-postgres-1
- infra-redis-1
- infra-mlflow-1
- infra-jaeger-1

---

## 3️⃣ Start Backend Server

```bash
cd backend
source venv/Scripts/activate
uvicorn main:app --reload
```

---

# 🌐 API Documentation

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# 🧪 Testing

## Test A/B Comparison

Endpoint:

```text
POST /pipelines/compare
```

Request:

```json
{
  "query": "What is AI?"
}
```

---

## Test Analytics

```text
GET /pipelines/test/analytics
```

---

## Test Runs History

```text
GET /pipelines/test/runs
```

---

# ✅ Expected Results

- Successful parallel pipeline execution
- Structured comparison output
- Evaluation scores generated
- Analytics metrics returned
- Run history tracked correctly

---

# 📂 Files Added

```text
backend/api/compare.py
backend/api/pipelines.py
backend/models/__init__.py
backend/models/pipeline.py
```

---

# 🚀 Final Outcome

Task 8 successfully implements a scalable and configurable Named Pipeline System for NeuroFlow with:

- strict schema validation
- async A/B comparison
- analytics support
- version-ready pipeline architecture
- evaluation integration

This creates the foundation for advanced experimentation and production-grade RAG pipeline management.
