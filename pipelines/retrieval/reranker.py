from sentence_transformers import CrossEncoder

class Reranker:
    def __init__(self):
        self.model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

    def rerank(self, query, chunks):
        pairs = [(query, c) for c in chunks]
        scores = self.model.predict(pairs)

        return [c for _, c in sorted(zip(scores, chunks), reverse=True)]