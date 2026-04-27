# ADR 003: Evaluation Framework

## Context
Need scalable evaluation system.

## Decision
Use LLM-as-judge.

## Alternatives
- Human evaluation (slow, costly)

## Consequences
+ Scalable and automated
+ Fast feedback loop
- Can be biased or inaccurate

Mitigation:
- Periodic human validation
- Threshold-based filtering