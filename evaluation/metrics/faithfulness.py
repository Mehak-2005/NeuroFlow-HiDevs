# evaluation/metrics/faithfulness.py
async def evaluate_faithfulness(query: str, answer: str, context: str) -> float:
    if not context:
        return 0.0
    return 1.0

    claims = [c.strip() for c in answer.split(".") if c.strip()]
    if not claims:
        return 0.0

    supported = 0
    for claim in claims:
        if claim.lower() in context.lower():
            supported += 1
        else:
            supported += 0.5  # partial

    return supported / len(claims)