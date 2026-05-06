# 🚀 Task 9 — Fine-Tuning Pipeline with MLflow Tracking & Model Registration

# 🚀 NeuroFlow — Advanced RAG System

## 📌 Project Overview

NeuroFlow is an advanced Retrieval-Augmented Generation (RAG) platform designed to support intelligent document ingestion, retrieval, generation, evaluation, and continuous fine-tuning workflows.

The system is built using:
- FastAPI
- PostgreSQL
- Redis
- MLflow
- Docker
- Async Python pipelines

NeuroFlow supports:
- multi-modal document ingestion
- hybrid retrieval pipelines
- streaming RAG generation
- automated evaluation
- configurable named pipelines
- fine-tuning workflows

The platform is designed for scalable AI systems that continuously improve through evaluation-driven learning.

---

# 🧠 System Architecture

```text
Document Upload
      ↓
Ingestion Pipeline
      ↓
Chunking & Embeddings
      ↓
Hybrid Retrieval
      ↓
RAG Generation
      ↓
Evaluation Framework
      ↓
Training Pair Extraction
      ↓
Fine-Tuning Pipeline
      ↓
Improved Models

```
# Project Structure 

NeuroFlow-HiDevs/
│
├── backend/
│   ├── api/
│   │   ├── ingest.py
│   │   ├── query.py
│   │   ├── compare.py
│   │   ├── pipelines.py
│   │   └── finetune.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── pipeline.py
│   │
│   ├── config.py
│   ├── main.py
│   └── requirements.txt
│
├── pipelines/
│   ├── ingestion/
│   ├── retrieval/
│   ├── generation/
│   └── finetuning/
│
├── evaluation/
│   ├── metrics/
│   ├── calibration/
│   └── judge.py
│
├── training_data/
│
├── infra/
│   └── docker-compose.yml
│
└── README.md

---
# Features Implemented
🔹 Task 9 — Fine-Tuning Pipeline

Implemented:

training pair extraction
JSONL dataset generation
MLflow experiment tracking
fine-tuning job management
artifact logging

Validation includes:

citation enforcement
PII filtering
quality threshold filtering
token length validation
---

# ⚙️ Technologies Used 

Backend
FastAPI
Python
asyncio
Databases
PostgreSQL
Redis
ML & AI
sentence-transformers
MLflow
RAG pipelines
Infrastructure
Docker
Docker Compose
Evaluation
RAGAS-inspired metrics
cosine similarity
Pearson correlation

---

# ▶️ Setup Instructions

1️⃣ Clone Repository
git clone <repo-url>
cd NeuroFlow-HiDevs

2️⃣ Start Infrastructure
cd infra
docker compose up -d

This starts:

PostgreSQL
Redis
MLflow
Jaeger

3️⃣ Activate Backend Environment
cd ../backend
source venv/Scripts/activate
4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Run Backend
uvicorn main:app --reload

---
# 🌐 API Documentation

Open Swagger UI:

http://127.0.0.1:8000/docs
🔌 Main API Endpoints
Ingestion
POST /ingest

Uploads and processes documents.

Query Generation
POST /query

Runs RAG generation.

Streaming Endpoint
GET /query/{run_id}/stream

Streams tokens using SSE.

Pipeline Comparison
POST /pipelines/compare

Runs A/B pipeline comparison.

Pipeline Analytics
GET /pipelines/{id}/analytics

Returns:

p50 latency
p95 latency
p99 latency
average evaluation score
Pipeline Runs
GET /pipelines/{id}/runs

Returns pipeline run history.

Fine-Tuning
POST /finetune

Starts fine-tuning job.

---
# 📄 Example Pipeline Compare Request
{
  "query": "What is AI?"
}

📄 Example Compare Output
{
  "query": "What is AI?",
  "pipeline_a": {
    "run_id": "123",
    "generation": "[A] Answer for: What is AI?",
    "retrieval_latency_ms": 500,
    "total_latency_ms": 1500,
    "chunks_used": 5,
    "eval_score": 0.85
  },
  "pipeline_b": {
    "run_id": "456",
    "generation": "[B] Answer for: What is AI?",
    "retrieval_latency_ms": 500,
    "total_latency_ms": 1500,
    "chunks_used": 5,
    "eval_score": 0.80
  }
}

📊 MLflow Tracking

Open MLflow dashboard:

http://localhost:5000

Tracks:

experiments
metrics
artifacts
training datasets
fine-tuning runs

🧪 Testing
Test Streaming
curl -N http://127.0.0.1:8000/query/{run_id}/stream

Test Health Endpoint
GET /health

Expected:

{
  "status": "ok",
  "checks": {
    "postgres": true,
    "redis": true,
    "mlflow": true
  }
}
---
# 📊 Evaluation Metrics

Implemented metrics:

Faithfulness
Answer Relevance
Context Precision
Context Recall

Overall score formula:

overall_score = (
    0.35 * faithfulness +
    0.30 * answer_relevance +
    0.20 * context_precision +
    0.15 * context_recall
)

📦 Fine-Tuning Dataset Format
{
  "messages": [
    {
      "role": "system",
      "content": "You are a precise research assistant..."
    },
    {
      "role": "user",
      "content": "[Question] What is AI?"
    },
    {
      "role": "assistant",
      "content": "AI is the simulation of human intelligence. [Source 1]"
    }
  ]
}

---
# 🔥 Key Highlights

✅ Multi-modal ingestion
✅ Hybrid retrieval system
✅ Streaming RAG generation
✅ Citation tracking
✅ Automated evaluation
✅ Named configurable pipelines
✅ Pipeline A/B comparison
✅ Fine-tuning workflow
✅ MLflow experiment tracking
✅ Dockerized infrastructure

---
#🎯 Learning Outcomes

This project demonstrates:

scalable RAG architecture
async backend systems
evaluation-driven AI pipelines
experiment tracking
retrieval optimization
streaming APIs
continuous model improvement

---
# 🛠 Future Improvements
Real LLM integrations
Production vector database
Real embeddings
Kubernetes deployment
Advanced analytics dashboard
Real-time monitoring
Model registry integration

---
#👨‍💻 Conclusion

NeuroFlow provides a complete end-to-end RAG infrastructure with:

ingestion
retrieval
generation
evaluation
fine-tuning

The platform demonstrates modern AI engineering workflows and scalable backend architecture for intelligent document systems.
---





