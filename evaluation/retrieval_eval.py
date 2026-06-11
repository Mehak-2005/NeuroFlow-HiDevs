import os
import sys
import asyncio

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

from pipelines.retrieval.retriever import Retriever


async def main():
    retriever = Retriever()

    results = await retriever.retrieve("What is AI?")

    print("RESULTS:")
    print(results)


if __name__ == "__main__":
    asyncio.run(main())