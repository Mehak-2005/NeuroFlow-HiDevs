import os
import sys

# ✅ ADD THIS FIRST
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import asyncio

from pipelines.retrieval.retriever import Retriever


async def main():
    r = Retriever()
    results = await r.retrieve("What is AI?")
    print("RESULTS:", results)


asyncio.run(main())
