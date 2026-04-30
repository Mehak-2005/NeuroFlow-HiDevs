import asyncio

from evaluation.metrics.faithfulness import evaluate_faithfulness
from evaluation.metrics.answer_relevance import evaluate_answer_relevance
from evaluation.metrics.context_precision import evaluate_context_precision
from evaluation.metrics.context_recall import evaluate_context_recall


class EvaluationJudge:

    async def evaluate(self, query, answer, chunks):
        context = " ".join(chunks)

        results = await asyncio.gather(
            evaluate_faithfulness(query, answer, context),
            evaluate_answer_relevance(query, answer),
            evaluate_context_precision(query, chunks, answer),
            evaluate_context_recall(query, chunks, answer)
        )

        faithfulness, answer_relevance, context_precision, context_recall = results

        # 🔥 DEBUG PRINT (you asked where to add this)
        print("Faithfulness:", faithfulness)
        print("Answer Relevance:", answer_relevance)
        print("Context Precision:", context_precision)
        print("Context Recall:", context_recall)

        overall_score = (
            0.35 * faithfulness +
            0.30 * answer_relevance +
            0.20 * context_precision +
            0.15 * context_recall
        )

        return {
            "faithfulness": faithfulness,
            "answer_relevance": answer_relevance,
            "context_precision": context_precision,
            "context_recall": context_recall,
            "overall_score": overall_score
        }