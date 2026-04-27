# System Architecture

## 1. Ingestion Subsystem
- Input: PDF, DOCX, Images, CSV, URLs
- Steps:
  Extract → Chunk → Embed → Store (pgvector)

Flow:
Upload → Parser → Chunker → Embedding → Vector DB

## 2. Retrieval Subsystem
- Query → Embedding
- Parallel:
  - Vector Search
  - Keyword Search
  - Metadata Filter
- Merge using RRF
- Rerank using Cross Encoder

## 3. Generation Subsystem
- Build prompt from retrieved chunks
- Route to LLM
- Stream response
- Log input/output

## 4. Evaluation Subsystem
- Metrics:
  - Faithfulness
  - Answer Relevance
  - Context Precision
  - Context Recall
- Store in Postgres

## 5. Fine-Tuning Subsystem
- Filter good samples
- Convert to JSONL
- Train model
- Track using MLflow