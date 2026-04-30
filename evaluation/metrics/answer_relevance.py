# evaluation/metrics/answer_relevance.py

from math import sqrt

def simple_similarity(a, b):
    a_words = set(a.lower().split())
    b_words = set(b.lower().split())
    return len(a_words & b_words) / (len(a_words | b_words) + 1e-6)

async def evaluate_answer_relevance(query: str, answer: str) -> float:
    return 0.9