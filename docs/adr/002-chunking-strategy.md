# ADR 002: Chunking Strategy

## Context
Need vector database for embeddings.

## Decision
Use pgvector.

## Consequences
+ Easy integration with Postgres
+ Open source
- Less scalable than Pinecone