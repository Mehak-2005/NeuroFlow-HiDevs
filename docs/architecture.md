# NeuroFlow System Architecture

## Overview
NeuroFlow is a modular RAG (Retrieval-Augmented Generation) system with evaluation and fine-tuning feedback loops.

---

## 1. Ingestion Subsystem

### Purpose
Convert raw data into searchable vector embeddings.

### Supported Inputs
- PDF, DOCX
- Images (OCR)
- CSV
- Web URLs

### Pipeline
Upload → Parsing → Chunking → Embedding → Storage

### Detailed Flow
1. User uploads file or URL
2. Parser extracts text (PyPDF, OCR, etc.)
3. Chunking strategy applied (semantic/fixed)
4. Each chunk converted into embedding
5. Stored in pgvector with metadata

### Data Flow Diagram
User Input
↓
Parser → Extracted Text
↓
Chunker → Text Chunks
↓
Embedding Model
↓
Vector Store (pgvector)


---

## 2. Retrieval Subsystem

### Purpose
Fetch most relevant context for a query

### Steps
1. Convert query to embedding
2. Run parallel searches:
   - Vector similarity search
   - Keyword search (BM25)
   - Metadata filtering
3. Combine results using Reciprocal Rank Fusion (RRF)
4. Apply cross-encoder reranker
5. Return top-k ranked chunks

### Flow
Query
↓
Embedding
↓
├── Vector Search
├── Keyword Search
└── Metadata Filter
↓
RRF Fusion
↓
Reranker
↓
Top Context

---

## 3. Generation Subsystem

### Purpose
Generate final answer using LLM

### Steps
1. Build prompt using:
   - User query
   - Retrieved context
2. Route to LLM based on:
   - Cost
   - Domain
3. Stream response token-by-token
4. Log:
   - Prompt
   - Response
   - Context used

---

## 4. Evaluation Subsystem

### Purpose
Measure output quality automatically

### Metrics
- Faithfulness
- Answer Relevance
- Context Precision
- Context Recall

### Flow
1. Take query, response, context
2. Run LLM-as-judge evaluation
3. Store scores in PostgreSQL
4. Compute rolling averages

---

## 5. Fine-Tuning Subsystem

### Purpose
Improve model over time

### Steps
1. Filter high-quality data:
   - Faithfulness > 0.8
   - User rating ≥ 4
2. Convert to JSONL
3. Submit fine-tuning job
4. Track experiments via MLflow
5. Route similar queries to fine-tuned model

---

## Tech Stack
- Backend: Python (FastAPI)
- Vector DB: pgvector
- Database: PostgreSQL
- ML Tracking: MLflow
- LLM APIs: OpenAI / others