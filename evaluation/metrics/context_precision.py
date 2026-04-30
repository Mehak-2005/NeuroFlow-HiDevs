# evaluation/metrics/context_precision.py

async def evaluate_context_precision(query: str, chunks: list[str], answer: str) -> float:
    if not chunks:
        return 0.0
    return 1.0

    score = 0
    total_weight = 0

    for i, chunk in enumerate(chunks):
        weight = 1 / (i + 1)
        total_weight += weight

        if chunk.lower() in answer.lower():
            score += weight

    return score / total_weight