async def test():
    pipeline = Retriever()

    results = await pipeline.retrieve("What is AI?")
    print(results)