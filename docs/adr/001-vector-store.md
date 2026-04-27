# ADR 001: Vector Store Selection

## Context
Need scalable vector database for embeddings.

## Decision
Use pgvector.

## Alternatives
- Pinecone (managed, costly)
- Weaviate (complex setup)
- Qdrant (good but extra infra)

## Consequences
+ Easy Postgres integration
+ Open-source and free
+ Good for small-medium scale
- Not as scalable as managed services