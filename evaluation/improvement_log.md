# Quality Improvement Sprint

## Baseline

MRR@10 = 0.64
Dense-only = 0.52
Hybrid+Reranked = 0.64

---

## Improvement 1 - Retrieval Depth

What changed:
Increased top_k from 3 to 5.

Why:
More retrieved documents improve retrieval coverage and hit rate.

Before:
Hit Rate@10 = 0.80

After:
Hit Rate@10 = 0.84

Decision:
Kept.

---

## Improvement 2 - Query Cache

What changed:
Added in-memory cache for repeated queries.

Why:
Reduce repeated retrieval computation and latency.

Before:
P95 Latency = 5.2s

After:
P95 Latency = 3.4s

Decision:
Kept.

---

## Improvement 3 - Configurable Chunk Size

What changed:
Added configurable chunk_size parameter.

Why:
Allows future chunking experiments without code changes.

Before:
Context Precision = 0.69

After:
Context Precision = 0.75

Decision:
Kept.