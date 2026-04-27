# ADR 002: Chunking Strategy

## Context
Chunking affects retrieval quality.

## Decision
Use semantic chunking primarily.

## Alternatives
- Fixed-size (fast but less accurate)
- Sentence-boundary (moderate)

## Consequences
+ Better context understanding
+ Higher retrieval accuracy
- Slightly slower

Switch to fixed-size if performance issues arise.