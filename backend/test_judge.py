import asyncio
import os
import sys

# FIX IMPORT PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from evaluation.judge import EvaluationJudge


async def test():
    judge = EvaluationJudge()

    result = await judge.evaluate(
        "What is AI?",
        "AI is simulation of human intelligence.",
        ["Artificial intelligence is simulation of human intelligence."],
    )

    print("\nFINAL RESULT:\n", result)


asyncio.run(test())
