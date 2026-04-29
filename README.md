# 📌 Task 6 — RAG Generation Pipeline (Streaming SSE + Citations)

## 🚀 Overview

This task implements the **Generation Pipeline** for a Retrieval-Augmented Generation (RAG) system.
It takes retrieved context (Task 5) and generates a **grounded, cited response** using streaming.

---

## 🧩 Features Implemented

### 1. Prompt Assembly

* Dynamic prompt building based on query type:

  * factual
  * analytical
  * comparative
  * procedural
* Context injected inside `<context>` tags
* Strict grounding:

  * No hallucination
  * Mandatory citations `[Source N]`

---

### 2. Streaming Generation (SSE)

* Implemented using **sse-starlette**
* Token-by-token streaming response
* Supports:

  * real-time output
  * long-running responses
  * keepalive events (prevents timeout)

---

### 3. SSE Events Flow

Example stream:

```
data: {"type": "retrieval_start"}

data: {"type": "retrieval_complete", "chunk_count": 3, "sources": ["doc1.pdf"]}

data: {"type": "token", "delta": "Artificial "}
data: {"type": "token", "delta": "intelligence "}

data: {"type": "done", "run_id": "abc-123", "citations": [...]}
```

---

### 4. Citation Tracking

* Extracts `[Source N]` from response
* Maps to:

  * chunk_id
  * document name
  * page number
* Flags invalid citations (hallucinations)

---

### 5. API Endpoints

#### ➤ POST `/query`

Request:

```json
{
  "query": "What is AI?",
  "pipeline_id": "123",
  "stream": true
}
```

Response:

* Returns `run_id`

---

#### ➤ GET `/query/{run_id}/stream`

* Streams response using SSE

Test:

```bash
curl -N http://127.0.0.1:8000/query/abc-123/stream
```

---

### 6. Health Check

```bash
GET /health
```

Example:

```json
{
  "status": "ok",
  "checks": {
    "postgres": true,
    "redis": true,
    "mlflow": true
  }
}
```

---

## ⚙️ Setup Instructions

```bash
git checkout task-35
git checkout -b task-36

cd backend
source venv/Scripts/activate   # Windows

pip install sse-starlette
pip freeze > requirements.txt
```

---

## ▶️ Run the Project

### Start Docker services:

```bash
cd infra
docker compose up -d
```

### Run backend:

```bash
cd ../backend
set PYTHONPATH=..
uvicorn main:app --reload
```

---

## 🧪 Testing Streaming

Open browser:

```
http://127.0.0.1:8000/query/abc-123/stream
```

OR:

```bash
curl -N http://127.0.0.1:8000/query/abc-123/stream
```

---

## 📁 Folder Structure

```
pipelines/
  generation/
    prompt_builder.py
    generator.py
    citations.py

backend/
  api/
    query.py
```

---

## ✅ Completion Checklist

* [x] Prompt builder implemented
* [x] Streaming SSE working
* [x] Token streaming verified
* [x] Citation parsing working
* [x] Invalid citations flagged
* [x] Health endpoint working

---

## 🎯 Output Example

```
Artificial intelligence is the simulation of human intelligence [Source 1]
```

With structured citations:

```json
[
  {
    "source": "Source 1",
    "chunk_id": "1",
    "document": "doc1.pdf",
    "page": 1
  }
]
```

---

## 📌 Conclusion

Task 6 successfully implements a **real-time streaming RAG generation pipeline** with:

* grounded responses
* citation tracking
* SSE-based streaming

---
