# 🛡️ Task 10 — Production Async Resilience
## Circuit Breakers, Rate Limiting & Backpressure

This task implements a production-grade resilience layer for NeuroFlow to handle provider failures, API rate limits, queue overload, and timeout management in distributed async environments.

---

# 🚀 Features Implemented

## ✅ Circuit Breaker System

Implemented Redis-backed circuit breakers for all external provider calls.

### Supported States
- CLOSED → normal operation
- OPEN → requests blocked after repeated failures
- HALF_OPEN → recovery testing state

### Features
- Failure threshold tracking
- Automatic recovery timeout
- Shared Redis state across workers
- Prevents cascading provider failures

### File
```text
backend/resilience/circuit_breaker.py
```
### ✅ Rate Limiting

Implemented token-bucket rate limiting using Redis.

Global Provider Limits

Supports provider-wide RPM control.

Example:
```
OpenAI → 3000 RPM
Per-Pipeline Limits
```
Each pipeline can define:
```
"rate_limit_rpm": 60
```
API Endpoint Limits

Endpoint	Limit

/ingest	10 requests/hour/IP
/query	60 requests/minute/IP
File
```
backend/resilience/rate_limiter.py
```

### ✅ Backpressure Protection

Protects ingestion workers from queue overload.

Queue Depth Rules
Queue Depth	Behavior
< 50	Normal
> 50	Warning response
> 100	503 Service Unavailable

Example Response
```
{
  "error": "ingestion_queue_full",
  "queue_depth": 120,
  "retry_after": 30
}
```
File
```
backend/resilience/backpressure.py

```

### ✅ Timeout Management

Added centralized timeout handling for all async provider calls.

Supported Timeout Types
Task Type	Timeout
Embedding	10s
Chat Completion	60s
Reranking	15s
Evaluation	120s
File Extraction	30s
URL Fetch	15s

Features
Uses asyncio.wait_for
Timeout tracking in Redis
Proper async exception propagation


File

```
backend/resilience/timeout_manager.py
```

### ✅ Enhanced Health Monitoring

Improved /health endpoint with resilience diagnostics.

Includes
PostgreSQL health
Redis health
MLflow health
Circuit breaker states
Queue depth
Worker count

Example Response

```
{
  "status": "ok",
  "checks": {
    "postgres": {
      "status": "ok",
      "latency_ms": 3
    },
    "redis": {
      "status": "ok",
      "latency_ms": 1
    },
    "mlflow": {
      "status": "ok",
      "latency_ms": 45
    },
    "circuit_breakers": {
      "openai": {
        "state": "closed",
        "failure_count": 0
      }
    },
    "queue_depth": 23,
    "worker_count": 2
  }
}
```
### ✅ Circuit Breaker Testing

Implemented unit testing for failure recovery.

Test Case
5 consecutive failures trigger OPEN state
6th call raises CircuitOpenError

File
```
backend/test_circuit_breaker.py
```
### 📂 Project Structure

backend/
│
├── resilience/
│   ├── __init__.py
│   ├── circuit_breaker.py
│   ├── rate_limiter.py
│   ├── backpressure.py
│   └── timeout_manager.py
│
├── test_circuit_breaker.py
└── main.py

### ⚙️ Technologies Used
FastAPI
Redis
AsyncIO
Docker
PostgreSQL
MLflow
Uvicorn

### ▶️ Running the Project

Start Infrastructure
```
cd infra
docker compose up -d
```
Activate Backend
```
cd backend
source venv/Scripts/activate
```
Run FastAPI Server
```
python -m uvicorn main:app --reload
```
### 🧪 Run Circuit Breaker Test
```
python test_circuit_breaker.py
```
Expected Output
```
Failure 1
Failure 2
Failure 3
Failure 4
Failure 5
CircuitOpenError triggered successfully
```
### 🌐 API Endpoints
Endpoint	Method	Description

/health	GET	Resilience system health
/query	POST	Rate-limited query endpoint
/ingest	POST	Queue-protected ingestion

### ✅ Task Completion Checklist

 Circuit breaker opens after 5 failures
 Redis-backed shared state
 Token bucket rate limiting
 Per-pipeline RPM control
 API endpoint rate limiting
 Queue backpressure protection
 Timeout management
 Enhanced /health endpoint
 Circuit breaker unit test
 GitHub branch pushed successfully

 ### 📌 Branch
 ```
task-10
```
### 👩‍💻 Author

Mehak-2005
NeuroFlow-HiDevs Project 🚀
