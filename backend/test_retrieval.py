import asyncio
from pipelines.retrieval.retriever import Retriever
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

async def main():
    r = Retriever()
    results = await r.retrieve("What is AI?")
    print("RESULTS:", results)

asyncio.run(main())