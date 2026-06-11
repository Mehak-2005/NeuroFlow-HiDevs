import numpy as np
from typing import List


class Retriever:
    def __init__(self):
        # ✅ Dummy document store (you can replace later with DB)
        self.documents = [
            "Artificial Intelligence is the simulation of human intelligence.",
            "Machine learning is a subset of AI that learns from data.",
            "Deep learning uses neural networks with many layers.",
            "Python is widely used in AI and data science.",
            "Transformers are powerful models used in NLP tasks."
        ]

        # ✅ Create simple embeddings (random for now)
        self.embeddings = [self._embed(doc) for doc in self.documents]

    def _embed(self, text: str) -> np.ndarray:
        # 🔹 Simple fake embedding (for now)
        np.random.seed(abs(hash(text)) % (10**6))
        return np.random.rand(128)

    def _cosine_similarity(self, a: np.ndarray, b: np.ndarray) -> float:
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    async def retrieve(self, query: str, top_k: int = 5) -> List[dict]:
        query_embedding = self._embed(query)

        scores = []
        for doc, emb in zip(self.documents, self.embeddings):
            sim = self._cosine_similarity(query_embedding, emb)
            scores.append((doc, sim))

        # 🔹 Sort by similarity
        scores.sort(key=lambda x: x[1], reverse=True)

        # 🔹 Return top results
        results = [
            {"text": doc, "score": float(score)}
            for doc, score in scores[:top_k]
        ]

        return results