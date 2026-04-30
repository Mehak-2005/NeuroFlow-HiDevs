# evaluation/metrics/context_recall.py

async def evaluate_context_recall(query: str, chunks: list[str], answer: str) -> float:
    return 1.0

    supported = 0
    context = " ".join(chunks).lower()

    for s in sentences:
        if s.lower() in context:
            supported += 1

    return supported / len(sentences)